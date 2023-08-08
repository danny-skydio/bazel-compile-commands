from bazel_protos import build_pb2 as _build_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = ["action_key", "arguments", "aspect_descriptor_ids", "configuration_id", "discovers_inputs", "environment_variables", "execution_info", "execution_platform", "file_contents", "input_dep_set_ids", "mnemonic", "output_ids", "param_files", "primary_output_id", "substitutions", "target_id", "template_content"]
    ACTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    ASPECT_DESCRIPTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOVERS_INPUTS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_DEP_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    MNEMONIC_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_IDS_FIELD_NUMBER: _ClassVar[int]
    PARAM_FILES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_OUTPUT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    action_key: str
    arguments: _containers.RepeatedScalarFieldContainer[str]
    aspect_descriptor_ids: _containers.RepeatedScalarFieldContainer[int]
    configuration_id: int
    discovers_inputs: bool
    environment_variables: _containers.RepeatedCompositeFieldContainer[KeyValuePair]
    execution_info: _containers.RepeatedCompositeFieldContainer[KeyValuePair]
    execution_platform: str
    file_contents: str
    input_dep_set_ids: _containers.RepeatedScalarFieldContainer[int]
    mnemonic: str
    output_ids: _containers.RepeatedScalarFieldContainer[int]
    param_files: _containers.RepeatedCompositeFieldContainer[ParamFile]
    primary_output_id: int
    substitutions: _containers.RepeatedCompositeFieldContainer[KeyValuePair]
    target_id: int
    template_content: str
    def __init__(self, target_id: _Optional[int] = ..., aspect_descriptor_ids: _Optional[_Iterable[int]] = ..., action_key: _Optional[str] = ..., mnemonic: _Optional[str] = ..., configuration_id: _Optional[int] = ..., arguments: _Optional[_Iterable[str]] = ..., environment_variables: _Optional[_Iterable[_Union[KeyValuePair, _Mapping]]] = ..., input_dep_set_ids: _Optional[_Iterable[int]] = ..., output_ids: _Optional[_Iterable[int]] = ..., discovers_inputs: bool = ..., execution_info: _Optional[_Iterable[_Union[KeyValuePair, _Mapping]]] = ..., param_files: _Optional[_Iterable[_Union[ParamFile, _Mapping]]] = ..., primary_output_id: _Optional[int] = ..., execution_platform: _Optional[str] = ..., template_content: _Optional[str] = ..., substitutions: _Optional[_Iterable[_Union[KeyValuePair, _Mapping]]] = ..., file_contents: _Optional[str] = ...) -> None: ...

class ActionGraphContainer(_message.Message):
    __slots__ = ["actions", "artifacts", "aspect_descriptors", "configuration", "dep_set_of_files", "path_fragments", "rule_classes", "targets"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    ASPECT_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DEP_SET_OF_FILES_FIELD_NUMBER: _ClassVar[int]
    PATH_FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    RULE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    artifacts: _containers.RepeatedCompositeFieldContainer[Artifact]
    aspect_descriptors: _containers.RepeatedCompositeFieldContainer[AspectDescriptor]
    configuration: _containers.RepeatedCompositeFieldContainer[Configuration]
    dep_set_of_files: _containers.RepeatedCompositeFieldContainer[DepSetOfFiles]
    path_fragments: _containers.RepeatedCompositeFieldContainer[PathFragment]
    rule_classes: _containers.RepeatedCompositeFieldContainer[RuleClass]
    targets: _containers.RepeatedCompositeFieldContainer[Target]
    def __init__(self, artifacts: _Optional[_Iterable[_Union[Artifact, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ..., targets: _Optional[_Iterable[_Union[Target, _Mapping]]] = ..., dep_set_of_files: _Optional[_Iterable[_Union[DepSetOfFiles, _Mapping]]] = ..., configuration: _Optional[_Iterable[_Union[Configuration, _Mapping]]] = ..., aspect_descriptors: _Optional[_Iterable[_Union[AspectDescriptor, _Mapping]]] = ..., rule_classes: _Optional[_Iterable[_Union[RuleClass, _Mapping]]] = ..., path_fragments: _Optional[_Iterable[_Union[PathFragment, _Mapping]]] = ...) -> None: ...

class Artifact(_message.Message):
    __slots__ = ["id", "is_tree_artifact", "path_fragment_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_TREE_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    PATH_FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_tree_artifact: bool
    path_fragment_id: int
    def __init__(self, id: _Optional[int] = ..., path_fragment_id: _Optional[int] = ..., is_tree_artifact: bool = ...) -> None: ...

class AspectDescriptor(_message.Message):
    __slots__ = ["id", "name", "parameters"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    parameters: _containers.RepeatedCompositeFieldContainer[KeyValuePair]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[KeyValuePair, _Mapping]]] = ...) -> None: ...

class Configuration(_message.Message):
    __slots__ = ["checksum", "id", "is_tool", "mnemonic", "platform_name"]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_TOOL_FIELD_NUMBER: _ClassVar[int]
    MNEMONIC_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    checksum: str
    id: int
    is_tool: bool
    mnemonic: str
    platform_name: str
    def __init__(self, id: _Optional[int] = ..., mnemonic: _Optional[str] = ..., platform_name: _Optional[str] = ..., checksum: _Optional[str] = ..., is_tool: bool = ...) -> None: ...

class ConfiguredTarget(_message.Message):
    __slots__ = ["configuration", "configuration_id", "target"]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    configuration: Configuration
    configuration_id: int
    target: _build_pb2.Target
    def __init__(self, target: _Optional[_Union[_build_pb2.Target, _Mapping]] = ..., configuration: _Optional[_Union[Configuration, _Mapping]] = ..., configuration_id: _Optional[int] = ...) -> None: ...

class CqueryResult(_message.Message):
    __slots__ = ["configurations", "results"]
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    configurations: _containers.RepeatedCompositeFieldContainer[Configuration]
    results: _containers.RepeatedCompositeFieldContainer[ConfiguredTarget]
    def __init__(self, results: _Optional[_Iterable[_Union[ConfiguredTarget, _Mapping]]] = ..., configurations: _Optional[_Iterable[_Union[Configuration, _Mapping]]] = ...) -> None: ...

class DepSetOfFiles(_message.Message):
    __slots__ = ["direct_artifact_ids", "id", "transitive_dep_set_ids"]
    DIRECT_ARTIFACT_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TRANSITIVE_DEP_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    direct_artifact_ids: _containers.RepeatedScalarFieldContainer[int]
    id: int
    transitive_dep_set_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., transitive_dep_set_ids: _Optional[_Iterable[int]] = ..., direct_artifact_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class KeyValuePair(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ParamFile(_message.Message):
    __slots__ = ["arguments", "exec_path"]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    EXEC_PATH_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedScalarFieldContainer[str]
    exec_path: str
    def __init__(self, exec_path: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...

class PathFragment(_message.Message):
    __slots__ = ["id", "label", "parent_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    label: str
    parent_id: int
    def __init__(self, id: _Optional[int] = ..., label: _Optional[str] = ..., parent_id: _Optional[int] = ...) -> None: ...

class RuleClass(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ["id", "label", "rule_class_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    RULE_CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    label: str
    rule_class_id: int
    def __init__(self, id: _Optional[int] = ..., label: _Optional[str] = ..., rule_class_id: _Optional[int] = ...) -> None: ...
