"""
Yet another compile_commands.json generator for Bazel.

This one uses aquery to get the compile commands for C++/C actions.
It relies on the structure of Middleman/CppCompile actions to relate headers to source files.
"""

import argparse
import functools
import json
import os
import re
import subprocess
import sys
import typing as T
from dataclasses import dataclass
from pathlib import Path
from queue import Queue

from google.protobuf import json_format

from bazel_protos.analysis_v2_pb2 import (
    Action,
    ActionGraphContainer,
    Artifact,
)

try:
    import argcomplete
except ImportError:
    argcomplete = None
try:
    from tqdm import tqdm # type: ignore
except ImportError:
    tqdm = None


_PROFILER = None
if "profile" in os.environ.get("DEBUG", ""):
    import cProfile

    _PROFILER = cProfile.Profile()
    _PROFILER.enable()


BUILD_WORKSPACE_DIRECTORY = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", os.getcwd()))


@dataclass(frozen=True)
class CompileCommandArgs:
    args: T.List[str]

    @functools.cached_property
    def args_encoded(self) -> str:
        return json.dumps(self.args)


@dataclass
class CompileCommand:
    path: str
    args: CompileCommandArgs


Munger = T.Callable[[T.Sequence[str]], T.List[str]]


def main(
    query: str,
    extra_aquery_args: T.List[str],
    munge_command_line: Munger,
    dump_aquery_output: T.Optional[Path],
    load_aquery_output: T.Optional[Path],
    proto_type: T.Literal["proto", "jsonproto"],
) -> None:
    exec_root = generate_exec_root()

    if load_aquery_output is not None:
        print("Loading aquery output...", file=sys.stderr)
        aquery_stdout = load_aquery_output.read_bytes()
    else:
        print("Running aquery...", file=sys.stderr)
        aquery_stdout = run_aquery(
            f"deps({query})", extra_args=extra_aquery_args, proto_type=proto_type
        )

    if dump_aquery_output is not None:
        dump_aquery_output.write_bytes(aquery_stdout)

    print("Parsing aquery output...", file=sys.stderr)
    aquery_output = parse_aquery(proto_type, aquery_stdout)

    print("Generating compile commands...", file=sys.stderr)
    if tqdm is not None:
        pbar = tqdm(total=len(aquery_output.actions))
    else:
        pbar = None

    # TODO(danny): relative paths should work, but the VSCode clangd plugin doesn't work right
    # if it finds compile_commands.json in a subdirectory (e.g. the example in this project).
    absolute_exec_root = str(exec_root.absolute())
    with open(BUILD_WORKSPACE_DIRECTORY / "compile_commands.json", "w", encoding="utf-8") as f:
        f.write("[\n")
        wrote_output = False
        for compile_command in process_actions(
            aquery_output,
            munge_command_line=munge_command_line,
            progress=pbar.update if pbar else None,
        ):
            wrote_output = True
            f.write(
                '{{"file": {}, "arguments": {}, "directory": {}}},\n'.format(
                    json.dumps(compile_command.path),
                    compile_command.args.args_encoded,
                    json.dumps(absolute_exec_root),
                )
            )
        # Remove trailing comma
        if wrote_output:
            f.seek(f.tell() - 2)
        f.write("\n]\n")

        if pbar is not None:
            pbar.close()


def generate_exec_root() -> Path:
    """Build things in the source tree, add a symlink to external."""
    exec_root = BUILD_WORKSPACE_DIRECTORY.absolute()
    (exec_root / "external").unlink(missing_ok=True)
    assert (exec_root / "bazel-out").is_symlink(), "bazel-out must exist and be a symlink"
    (exec_root / "external").symlink_to(BUILD_WORKSPACE_DIRECTORY / "bazel-out/../../../external")

    return exec_root


def run_aquery(
    target_label: str, extra_args: T.List[str], proto_type: T.Literal["proto", "jsonproto"]
) -> bytes:
    aquery_args = [
        "bazel",
        "aquery",
        # Filter to only C++/C compiles and Middleman actions.
        # Middleman actions are used to wrap headers of cc_library targets.
        f"mnemonic('CppCompile|Middleman', {target_label})",
        f"--output={proto_type}",
    ] + extra_args

    try:
        aquery_stdout = subprocess.check_output(aquery_args, cwd=BUILD_WORKSPACE_DIRECTORY)
    except subprocess.CalledProcessError as err:
        print(f"aquery exited with status {err.returncode}, ignoring", file=sys.stderr)
        aquery_stdout = err.stdout

    return aquery_stdout


def parse_aquery(
    proto_type: T.Literal["proto", "jsonproto"], aquery_stdout: bytes
) -> ActionGraphContainer:
    parsed_aquery_output = ActionGraphContainer()
    if proto_type == "proto":
        parsed_aquery_output.ParseFromString(aquery_stdout)
    elif proto_type == "jsonproto":
        json_format.Parse(aquery_stdout, parsed_aquery_output)
    else:
        raise ValueError(f"Unknown proto_type {proto_type}")

    return parsed_aquery_output


class ActionGraph:
    def __init__(self, aquery_output: ActionGraphContainer) -> None:
        self.file_depsets = {depset.id: depset for depset in aquery_output.dep_set_of_files}
        self.artifacts = {artifact.id: artifact for artifact in aquery_output.artifacts}
        self.path_fragments = {fragment.id: fragment for fragment in aquery_output.path_fragments}

        self.targets_by_id = {target.id: target for target in aquery_output.targets}

        self.action_for_artifact: T.Dict[int, Action] = {}
        for action in aquery_output.actions:
            for output_id in action.output_ids:
                self.action_for_artifact[output_id] = action

        self._artifact_path_cache: T.Dict[int, str] = {}

    def get_artifacts(
        self,
        depset_id: int,
        visited: T.Optional[T.Set[int]],
        depth: int = 0,
        depth_limit: T.Optional[int] = None,
    ) -> T.Iterable[Artifact]:
        if visited is not None:
            if depset_id in visited:
                return []

            visited.add(depset_id)

        for artifact_id in self.file_depsets[depset_id].direct_artifact_ids:
            yield self.artifacts[artifact_id]

        if depth_limit is None or depth < depth_limit:
            for transitive_depset_id in self.file_depsets[depset_id].transitive_dep_set_ids:
                yield from self.get_artifacts(transitive_depset_id, visited, depth + 1)

    def _get_full_path(self, path_fragment_id: int) -> str:
        fragment = self.path_fragments[path_fragment_id]

        if fragment.parent_id:
            if fragment.id not in self._artifact_path_cache:
                self._artifact_path_cache[fragment.id] = os.path.join(
                    self._get_full_path(fragment.parent_id), fragment.label
                )
            return self._artifact_path_cache[fragment.id]
        else:
            return fragment.label

    def get_artifact_path(self, artifact: Artifact) -> str:
        return self._get_full_path(artifact.path_fragment_id)

    def explore_input_level(
        self, action: Action, visited_depsets: T.Optional[T.Set[int]]
    ) -> T.Tuple[T.List[Artifact], T.List[Action]]:
        input_artifacts = []
        unexplored_actions = []
        for input_depset_id in action.input_dep_set_ids:
            for artifact in self.get_artifacts(input_depset_id, visited_depsets):
                if artifact.id in self.action_for_artifact:
                    unexplored_actions.append(self.action_for_artifact[artifact.id])
                else:
                    input_artifacts.append(artifact)

        return input_artifacts, unexplored_actions


def _get_compile_command(action: Action, munge_command_line: Munger) -> CompileCommand:
    """Get the compile command for a CppCompile action."""
    compile_args = munge_command_line(action.arguments)
    # We get the source file from the -c argument, as we're not guaranteed to have source
    # files in the input depsets since Middleman actions only have headers.
    source_file: T.Optional[str] = None
    for i, arg in enumerate(compile_args):
        if arg == "-c":
            source_file = compile_args[i + 1]
            break

    assert source_file is not None
    return CompileCommand(
        path=source_file,
        args=CompileCommandArgs(compile_args),
    )


def _debug_skipped(
    aquery_output: ActionGraphContainer,
    ag: ActionGraph,
    unseen_actions: T.Set[int],
    increment_completed_actions: T.Callable[[], None],
) -> None:
    """
    Debugging function to collect info about files that weren't seen during BFS.
    The reason these exist is because bazel does other things with Middleman actions besides
    wrapping headers.

    At the time of writing, the files we're skipping seem fine to skip, but it seems worth keeping
    this debugging code in case that changes.
    """
    all_actions = {a.primary_output_id: a for a in aquery_output.actions}
    skipped_files: T.Set[str] = set()

    for unseen_action_id in unseen_actions:
        increment_completed_actions()
        action = all_actions[unseen_action_id]
        direct_inputs, _ = ag.explore_input_level(action, visited_depsets=None)
        for direct_input in direct_inputs:
            artifact_path = ag.get_artifact_path(direct_input)
            if artifact_path.endswith("/MANIFEST"):
                continue
            skipped_files.add(artifact_path)

    skipped_files_string = "\n".join(sorted(skipped_files))
    print(
        f"Skipped {len(skipped_files)} interesting looking files:\n{skipped_files_string}",
        file=sys.stderr,
    )


def process_actions(
    aquery_output: ActionGraphContainer,
    munge_command_line: Munger,
    progress: T.Optional[T.Callable[[T.Optional[float]], T.Optional[bool]]] = None,
) -> T.Iterable[CompileCommand]:
    """
    Breadth-first search through action inputs.

    First, we do the easy thing and yield compile commands for all files that
    are direct inputs to the action.

    Then, we do a BFS through indirect action inputs. Bazel helpfully wraps
    header-only libraries in Middleman actions, so we unwrap one level each
    pass through the loop.

    If the direct inputs of the Middleman actions haven't been assigned yet, we
    assign them to the parent action's compile command and move on. We check
    every artifact until we've exhausted all unexplored leaves.

    If bazel stops using Middleman actions, this could probably be reworked to
    do a DFS on the depsets instead of actions.
    """
    ag = ActionGraph(aquery_output)
    queue: Queue[Action] = Queue()
    # primary_output_id is pretty much a unique identifier for an action
    artifact_compile_roots: T.Dict[int, int] = {}  # artifact_id -> primary_output_id
    # primary_output_id -> primary_output_id/compile args
    compile_roots: T.Dict[int, T.Union[int, CompileCommandArgs]] = {}

    unseen_actions = set(a.primary_output_id for a in aquery_output.actions)

    def increment_completed_actions() -> None:
        if progress is not None:
            progress(1)  # for tqdm-style progress.

    for action in aquery_output.actions:
        if action.mnemonic == "CppCompile":
            unseen_actions.remove(action.primary_output_id)
            compile_command = _get_compile_command(action, munge_command_line)
            compile_roots[action.primary_output_id] = compile_command.args
            queue.put(action)
            increment_completed_actions()
        else:
            assert action.mnemonic == "Middleman"

    visited_depsets: T.Set[int] = set()

    while not queue.empty():
        action = queue.get()
        direct_inputs, unexplored_actions = ag.explore_input_level(action, visited_depsets)
        for artifact in direct_inputs:  # direct sources and headers
            if artifact.id in artifact_compile_roots:
                continue
            artifact_compile_roots[artifact.id] = action.primary_output_id

        for unexplored_action in unexplored_actions:
            if unexplored_action.primary_output_id in compile_roots:
                continue
            unseen_actions.remove(unexplored_action.primary_output_id)
            compile_roots[unexplored_action.primary_output_id] = action.primary_output_id
            queue.put(unexplored_action)
            increment_completed_actions()

    # Now that we've explored all the actions, we can build the compile commands
    for artifact_id, action_id in artifact_compile_roots.items():
        id_or_args: T.Union[int, CompileCommandArgs] = action_id
        while not isinstance(id_or_args, CompileCommandArgs):
            id_or_args = compile_roots[id_or_args]
        yield CompileCommand(
            path=ag.get_artifact_path(ag.artifacts[artifact_id]),
            args=id_or_args,
        )

    # NOTE(danny): There are some actions that aren't reachable from CppCompile actions.
    # We don't really care about these, but we aggregate them here for debugging purposes.
    if "skipped" in os.environ.get("DEBUG", ""):
        _debug_skipped(aquery_output, ag, unseen_actions, increment_completed_actions)
    else:
        for _ in unseen_actions:
            increment_completed_actions()


def create_command_line_munger(
    exclude_args: T.Set[str], exclude_system_includes: T.Set[str]
) -> Munger:
    exclude_args_re = re.compile("|".join(exclude_args))

    def filter_problematic_args(compile_args: T.Sequence[str]) -> T.List[str]:
        skip_next = False
        new_compile_args = []
        for index in range(len(compile_args)):
            arg = compile_args[index]

            if (
                index < len(compile_args) - 1
                and arg == "-isystem"
                and compile_args[index + 1] in exclude_system_includes
            ):
                skip_next = True
                continue  # unnecesary, but explicit
            elif skip_next:
                skip_next = False
                continue
            else:
                if exclude_args_re.match(arg):
                    continue

                new_compile_args.append(arg)
        return new_compile_args

    return filter_problematic_args


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "query",
        nargs="?",
        help="Bazel query target to generate compile commands for",
        default="//... except attr(tags, '\\bmanual\\b', //...)",
    )
    parser.add_argument(
        "--extra_aquery_arg",
        help="Extra argument to pass to aquery (can be used multiple times)",
        action="append",
        default=[],
    )
    parser.add_argument(
        "--exclude_system_include",
        help="Filter out '-isystem' arguments with this value (can be used multiple times)",
        action="append",
        default=[],
    )
    parser.add_argument(
        "--exclude_compile_arg",
        help="Filter out this compile argument from output (can be used multiple times)",
        action="append",
        default=[],
    )
    parser.add_argument("--dump_aquery_output", help="Dump aquery output to this file", type=Path)
    parser.add_argument("--load_aquery_output", help="Load aquery output from this file", type=Path)

    # TODO(danny): https://github.com/bazelbuild/bazel/issues/18930
    # The binary proto format is much faster, but it seems broken for certain queries.
    # We're setting it as the default for now, but if you see issues, try jsonproto.
    parser.add_argument(
        "--proto_type", help="aquery output format", default="proto", choices=("proto", "jsonproto")
    )

    if argcomplete is not None:
        argcomplete.autocomplete(parser)
    args = parser.parse_args()

    try:
        main(
            args.query,
            extra_aquery_args=args.extra_aquery_arg,
            munge_command_line=create_command_line_munger(
                exclude_args=set(
                    args.exclude_compile_arg
                    + [
                        # Always filter out -fno-canonical-system-headers
                        # It's a gcc option that confuses clangd. It's added by Bazel's default host
                        # toolchain. clang doesn't need this option, as it does the right thing by
                        # default.
                        "-fno-canonical-system-headers",
                    ]
                ),
                # We've seen bad behavior when clangd uses --query-driver to add system headers.
                # We use this to remove includes that break `#include_next`.
                # See https://discourse.llvm.org/t/in-included-file-stdlib-h-file-not-found/1694/6
                exclude_system_includes=set(args.exclude_system_include),
            ),
            dump_aquery_output=args.dump_aquery_output,
            load_aquery_output=args.load_aquery_output,
            proto_type=args.proto_type,
        )
    except KeyboardInterrupt:
        pass
    if _PROFILER is not None:
        profile_path = "/tmp/compile_commands.prof"
        print(f"Dumping profile to {profile_path}", file=sys.stderr)
        _PROFILER.dump_stats(profile_path)
