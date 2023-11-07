# bazel-compile-commands
Another bazel compile_commands.json extractor.

This is not an officially supported Skydio product in any way.

## Usage
```python
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_compile_commands",
    sha256 = "5156fcba061198ea649ecc95762ef228c4b1b49c8cdf9197810e1b8112a1033a",
    strip_prefix = "bazel-compile-commands-f769e151d5784ec6645be08c43bf869acea800ef",
    urls = ["https://github.com/danny-skydio/bazel-compile-commands/archive/f769e151d5784ec6645be08c43bf869acea800ef.tar.gz"],
)

load("@bazel_compile_commands//:deps.bzl", "bazel_compile_commands_dependencies")

# We need rules_python and com_google_protobuf, if you have other versions it should be okay.
# If you want other versions, load them before calling bazel_compile_commands_dependencies!
bazel_compile_commands_dependencies()

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

# Python 3.8+ should work.
python_register_toolchains(
    name = "python_3_11",
    python_version = "3.11",
)

load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")

rules_proto_dependencies()

rules_proto_toolchains()
```

The way the script is set up requires you to have your outputs be mapped into a folder called `build`. In .bazelrc:
```
# Move build artifacts to the build directory
build --symlink_prefix=build/bazel-
```

If you're using the [VS Code clangd plugin](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd), in .vscode/settings.json:
```
  "clangd.arguments": [
    // Remap go-to-definition paths out of the clangd_execroot folder.
    "--path-mappings=${workspaceFolder}/build/bazel-out=${workspaceFolder}/build/clangd_execroot/bazel-out,${workspaceFolder}/build/bazel-out/../../../external=${workspaceFolder}/build/clangd_execroot/external,${workspaceFolder}=${workspaceFolder}/build/clangd_execroot",
    // Allow clangd to execute your compiler to find system headers. I've seen strange errors when this is enabled, so it might be worth trying without it.
    "--query-driver=/**"
  ],
```

To run, use `bazel run @bazel_compile_commands//:generate_compile_commands -- //...`

You may find in large repos that `//...` is too much, and you need to run it on a subset of your repo.
See the [bazel aquery docs](https://bazel.build/query/aquery) for more information on how to use aquery.
The query is wrapped with `deps()`, but filtered down to `CppCompile` and `Middleman` actions.

This tool is not particularly configurable, feel free to fork it and modify it to your needs.

## Details

This tool uses `bazel aquery` to get the actual command lines that will be used to compile each file.
The major complication is that we want to give clangd context for how header files are used in the project.
The way we solve this problem is by assocating every header with the command line of a source file (.cc/.cpp) that includes it.
We trace through the whole dependency tree, for headers included in sources, we associate them directly, for headers included in other headers, we trace back up the tree until we find a source file.

We use pre-compiled protobuf outputs. To regenerate them, use `./regenerate_protos.sh` (run from the root of the repo).
This requires [nix](https://nixos.org/download) to be installed.

## Known issues

- Headers stored in tree artifacts are not expanded, so there won't be an entry in compile_commands.json for them.
- `cc_library`s using `strip_include_prefix` should work (if they've been built recently), but clicking through will open the generated `_virtual_includes` folder, not the original source (if it exists).

## Related projects

- [hedronvision/bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor)
- [grailbio/bazel-compilation-database](https://github.com/grailbio/bazel-compilation-database)
- [stackb/bazel-stack-vscode-cc](https://github.com/stackb/bazel-stack-vscode-cc)
