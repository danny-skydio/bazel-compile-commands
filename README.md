# bazel-compile-commands
Another bazel compile_commands.json extractor.

This is not an officially supported Skydio product in any way.

## Usage
See [releases](https://github.com/danny-skydio/bazel-compile-commands/releases) for install information.

If you're using the [VS Code clangd plugin](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd), you may want to experiment with this option in .vscode/settings.json:
```
  "clangd.arguments": [
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
