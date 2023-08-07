#!/bin/sh
# Regenerate protobuf outputs.
# Requires nix to be installed.

NIX_REVISION="7721e0d2c1845c24eafd5a016b9d349187c48097"
PROTOC_COMMAND="protoc --python_out=. --pyi_out=. bazel_protos/build.proto bazel_protos/analysis_v2.proto"

nix-shell -p protobuf -I nixpkgs="https://github.com/NixOS/nixpkgs/archive/$NIX_REVISION.tar.gz" --run "$PROTOC_COMMAND"
