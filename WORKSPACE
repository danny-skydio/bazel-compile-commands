load("@//:deps.bzl", "bazel_compile_commands_dependencies")

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
