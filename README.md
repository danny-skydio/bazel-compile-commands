# bazel-compile-commands
Another bazel compile_commands.json extractor.

## Usage
```python

```

In .vscode/settings.json:
```
  "clangd.arguments": [
    "--path-mappings=${workspaceFolder}/build/bazel-out=${workspaceFolder}/build/clangd_execroot/bazel-out,${workspaceFolder}/build/bazel-out/../../../external=${workspaceFolder}/build/clangd_execroot/external,${workspaceFolder}=${workspaceFolder}/build/clangd_execroot",
    "--query-driver=/**"
  ],
```

## Details

This tool uses `bazel aquery` to get the actual command lines that will be used to compile each file.
The major complication is that we want to give clangd context for how header files are used in the project.
The way we solve this problem is by assocating every header with the command line of a source file (.cc/.cpp) that includes it.
We trace through the whole dependency tree, for headers included in sources, we associate them directly, for headers included in other headers, we trace back up the tree until we find a source file.

We use pre-compiled protobuf outputs. To regenerate them, use `./regenerate_protos.sh` (run from the root of the repo).
This requires [nix](https://nixos.org/download) to be installed.
