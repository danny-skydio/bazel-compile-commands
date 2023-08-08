from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllowedRuleClassInfo(_message.Message):
    __slots__ = ["allowed_rule_class", "policy"]
    class AllowedRuleClasses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALLOWED_RULE_CLASS_FIELD_NUMBER: _ClassVar[int]
    ANY: AllowedRuleClassInfo.AllowedRuleClasses
    POLICY_FIELD_NUMBER: _ClassVar[int]
    SPECIFIED: AllowedRuleClassInfo.AllowedRuleClasses
    allowed_rule_class: _containers.RepeatedScalarFieldContainer[str]
    policy: AllowedRuleClassInfo.AllowedRuleClasses
    def __init__(self, policy: _Optional[_Union[AllowedRuleClassInfo.AllowedRuleClasses, str]] = ..., allowed_rule_class: _Optional[_Iterable[str]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["DEPRECATED_string_dict_unary_value", "boolean_value", "explicitly_specified", "fileset_list_value", "int_list_value", "int_value", "label_dict_unary_value", "label_keyed_string_dict_value", "label_list_dict_value", "license", "name", "nodep", "selector_list", "string_dict_value", "string_list_dict_value", "string_list_value", "string_value", "tristate_value", "type"]
    class Discriminator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Tristate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Selector(_message.Message):
        __slots__ = ["entries", "has_default_value", "no_match_error"]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        HAS_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        NO_MATCH_ERROR_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[Attribute.SelectorEntry]
        has_default_value: bool
        no_match_error: str
        def __init__(self, entries: _Optional[_Iterable[_Union[Attribute.SelectorEntry, _Mapping]]] = ..., has_default_value: bool = ..., no_match_error: _Optional[str] = ...) -> None: ...
    class SelectorEntry(_message.Message):
        __slots__ = ["DEPRECATED_string_dict_unary_value", "boolean_value", "fileset_list_value", "int_list_value", "int_value", "is_default_value", "label", "label_dict_unary_value", "label_keyed_string_dict_value", "label_list_dict_value", "license", "string_dict_value", "string_list_dict_value", "string_list_value", "string_value", "tristate_value"]
        BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_STRING_DICT_UNARY_VALUE_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_string_dict_unary_value: _containers.RepeatedScalarFieldContainer[bytes]
        FILESET_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        LABEL_DICT_UNARY_VALUE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LABEL_KEYED_STRING_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
        LABEL_LIST_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
        LICENSE_FIELD_NUMBER: _ClassVar[int]
        STRING_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_LIST_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        TRISTATE_VALUE_FIELD_NUMBER: _ClassVar[int]
        boolean_value: bool
        fileset_list_value: _containers.RepeatedCompositeFieldContainer[FilesetEntry]
        int_list_value: _containers.RepeatedScalarFieldContainer[int]
        int_value: int
        is_default_value: bool
        label: str
        label_dict_unary_value: _containers.RepeatedCompositeFieldContainer[LabelDictUnaryEntry]
        label_keyed_string_dict_value: _containers.RepeatedCompositeFieldContainer[LabelKeyedStringDictEntry]
        label_list_dict_value: _containers.RepeatedCompositeFieldContainer[LabelListDictEntry]
        license: License
        string_dict_value: _containers.RepeatedCompositeFieldContainer[StringDictEntry]
        string_list_dict_value: _containers.RepeatedCompositeFieldContainer[StringListDictEntry]
        string_list_value: _containers.RepeatedScalarFieldContainer[str]
        string_value: str
        tristate_value: Attribute.Tristate
        def __init__(self, label: _Optional[str] = ..., is_default_value: bool = ..., int_value: _Optional[int] = ..., string_value: _Optional[str] = ..., boolean_value: bool = ..., tristate_value: _Optional[_Union[Attribute.Tristate, str]] = ..., string_list_value: _Optional[_Iterable[str]] = ..., license: _Optional[_Union[License, _Mapping]] = ..., string_dict_value: _Optional[_Iterable[_Union[StringDictEntry, _Mapping]]] = ..., fileset_list_value: _Optional[_Iterable[_Union[FilesetEntry, _Mapping]]] = ..., label_list_dict_value: _Optional[_Iterable[_Union[LabelListDictEntry, _Mapping]]] = ..., string_list_dict_value: _Optional[_Iterable[_Union[StringListDictEntry, _Mapping]]] = ..., int_list_value: _Optional[_Iterable[int]] = ..., label_dict_unary_value: _Optional[_Iterable[_Union[LabelDictUnaryEntry, _Mapping]]] = ..., label_keyed_string_dict_value: _Optional[_Iterable[_Union[LabelKeyedStringDictEntry, _Mapping]]] = ..., DEPRECATED_string_dict_unary_value: _Optional[_Iterable[bytes]] = ...) -> None: ...
    class SelectorList(_message.Message):
        __slots__ = ["elements", "type"]
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[Attribute.Selector]
        type: Attribute.Discriminator
        def __init__(self, type: _Optional[_Union[Attribute.Discriminator, str]] = ..., elements: _Optional[_Iterable[_Union[Attribute.Selector, _Mapping]]] = ...) -> None: ...
    AUTO: Attribute.Tristate
    BOOLEAN: Attribute.Discriminator
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_STRING_DICT_UNARY: Attribute.Discriminator
    DEPRECATED_STRING_DICT_UNARY_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_string_dict_unary_value: _containers.RepeatedScalarFieldContainer[bytes]
    DISTRIBUTION_SET: Attribute.Discriminator
    EXPLICITLY_SPECIFIED_FIELD_NUMBER: _ClassVar[int]
    FILESET_ENTRY_LIST: Attribute.Discriminator
    FILESET_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER: Attribute.Discriminator
    INTEGER_LIST: Attribute.Discriminator
    INT_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL: Attribute.Discriminator
    LABEL_DICT_UNARY: Attribute.Discriminator
    LABEL_DICT_UNARY_VALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL_KEYED_STRING_DICT: Attribute.Discriminator
    LABEL_KEYED_STRING_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL_LIST: Attribute.Discriminator
    LABEL_LIST_DICT: Attribute.Discriminator
    LABEL_LIST_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
    LICENSE: Attribute.Discriminator
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO: Attribute.Tristate
    NODEP_FIELD_NUMBER: _ClassVar[int]
    OUTPUT: Attribute.Discriminator
    OUTPUT_LIST: Attribute.Discriminator
    SELECTOR_LIST: Attribute.Discriminator
    SELECTOR_LIST_FIELD_NUMBER: _ClassVar[int]
    STRING: Attribute.Discriminator
    STRING_DICT: Attribute.Discriminator
    STRING_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST: Attribute.Discriminator
    STRING_LIST_DICT: Attribute.Discriminator
    STRING_LIST_DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    TRISTATE: Attribute.Discriminator
    TRISTATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Attribute.Discriminator
    YES: Attribute.Tristate
    boolean_value: bool
    explicitly_specified: bool
    fileset_list_value: _containers.RepeatedCompositeFieldContainer[FilesetEntry]
    int_list_value: _containers.RepeatedScalarFieldContainer[int]
    int_value: int
    label_dict_unary_value: _containers.RepeatedCompositeFieldContainer[LabelDictUnaryEntry]
    label_keyed_string_dict_value: _containers.RepeatedCompositeFieldContainer[LabelKeyedStringDictEntry]
    label_list_dict_value: _containers.RepeatedCompositeFieldContainer[LabelListDictEntry]
    license: License
    name: str
    nodep: bool
    selector_list: Attribute.SelectorList
    string_dict_value: _containers.RepeatedCompositeFieldContainer[StringDictEntry]
    string_list_dict_value: _containers.RepeatedCompositeFieldContainer[StringListDictEntry]
    string_list_value: _containers.RepeatedScalarFieldContainer[str]
    string_value: str
    tristate_value: Attribute.Tristate
    type: Attribute.Discriminator
    def __init__(self, name: _Optional[str] = ..., explicitly_specified: bool = ..., nodep: bool = ..., type: _Optional[_Union[Attribute.Discriminator, str]] = ..., int_value: _Optional[int] = ..., string_value: _Optional[str] = ..., boolean_value: bool = ..., tristate_value: _Optional[_Union[Attribute.Tristate, str]] = ..., string_list_value: _Optional[_Iterable[str]] = ..., license: _Optional[_Union[License, _Mapping]] = ..., string_dict_value: _Optional[_Iterable[_Union[StringDictEntry, _Mapping]]] = ..., fileset_list_value: _Optional[_Iterable[_Union[FilesetEntry, _Mapping]]] = ..., label_list_dict_value: _Optional[_Iterable[_Union[LabelListDictEntry, _Mapping]]] = ..., string_list_dict_value: _Optional[_Iterable[_Union[StringListDictEntry, _Mapping]]] = ..., int_list_value: _Optional[_Iterable[int]] = ..., label_dict_unary_value: _Optional[_Iterable[_Union[LabelDictUnaryEntry, _Mapping]]] = ..., label_keyed_string_dict_value: _Optional[_Iterable[_Union[LabelKeyedStringDictEntry, _Mapping]]] = ..., selector_list: _Optional[_Union[Attribute.SelectorList, _Mapping]] = ..., DEPRECATED_string_dict_unary_value: _Optional[_Iterable[bytes]] = ...) -> None: ...

class AttributeDefinition(_message.Message):
    __slots__ = ["allow_empty", "allow_single_file", "allowed_rule_classes", "cfg_is_host", "configurable", "default", "documentation", "executable", "mandatory", "name", "nodep", "type"]
    ALLOWED_RULE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EMPTY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SINGLE_FILE_FIELD_NUMBER: _ClassVar[int]
    CFG_IS_HOST_FIELD_NUMBER: _ClassVar[int]
    CONFIGURABLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_FIELD_NUMBER: _ClassVar[int]
    MANDATORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODEP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    allow_empty: bool
    allow_single_file: bool
    allowed_rule_classes: AllowedRuleClassInfo
    cfg_is_host: bool
    configurable: bool
    default: AttributeValue
    documentation: str
    executable: bool
    mandatory: bool
    name: str
    nodep: bool
    type: Attribute.Discriminator
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[Attribute.Discriminator, str]] = ..., mandatory: bool = ..., allowed_rule_classes: _Optional[_Union[AllowedRuleClassInfo, _Mapping]] = ..., documentation: _Optional[str] = ..., allow_empty: bool = ..., allow_single_file: bool = ..., default: _Optional[_Union[AttributeValue, _Mapping]] = ..., executable: bool = ..., configurable: bool = ..., nodep: bool = ..., cfg_is_host: bool = ...) -> None: ...

class AttributeValue(_message.Message):
    __slots__ = ["bool", "dict", "int", "list", "string"]
    class DictEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttributeValue, _Mapping]] = ...) -> None: ...
    BOOL_FIELD_NUMBER: _ClassVar[int]
    DICT_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    dict: _containers.RepeatedCompositeFieldContainer[AttributeValue.DictEntry]
    int: int
    list: _containers.RepeatedCompositeFieldContainer[AttributeValue]
    string: str
    def __init__(self, int: _Optional[int] = ..., string: _Optional[str] = ..., bool: bool = ..., list: _Optional[_Iterable[_Union[AttributeValue, _Mapping]]] = ..., dict: _Optional[_Iterable[_Union[AttributeValue.DictEntry, _Mapping]]] = ...) -> None: ...

class BuildLanguage(_message.Message):
    __slots__ = ["rule"]
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _containers.RepeatedCompositeFieldContainer[RuleDefinition]
    def __init__(self, rule: _Optional[_Iterable[_Union[RuleDefinition, _Mapping]]] = ...) -> None: ...

class ConfiguredRuleInput(_message.Message):
    __slots__ = ["configuration_checksum", "configuration_id", "label"]
    CONFIGURATION_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    configuration_checksum: str
    configuration_id: int
    label: str
    def __init__(self, label: _Optional[str] = ..., configuration_checksum: _Optional[str] = ..., configuration_id: _Optional[int] = ...) -> None: ...

class EnvironmentGroup(_message.Message):
    __slots__ = ["default", "environment", "name"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    default: _containers.RepeatedScalarFieldContainer[str]
    environment: _containers.RepeatedScalarFieldContainer[str]
    name: str
    def __init__(self, name: _Optional[str] = ..., environment: _Optional[_Iterable[str]] = ..., default: _Optional[_Iterable[str]] = ...) -> None: ...

class FilesetEntry(_message.Message):
    __slots__ = ["destination_directory", "exclude", "file", "files_present", "source", "strip_prefix", "symlink_behavior"]
    class SymlinkBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COPY: FilesetEntry.SymlinkBehavior
    DEREFERENCE: FilesetEntry.SymlinkBehavior
    DESTINATION_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    FILES_PRESENT_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STRIP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    destination_directory: str
    exclude: _containers.RepeatedScalarFieldContainer[str]
    file: _containers.RepeatedScalarFieldContainer[str]
    files_present: bool
    source: str
    strip_prefix: str
    symlink_behavior: FilesetEntry.SymlinkBehavior
    def __init__(self, source: _Optional[str] = ..., destination_directory: _Optional[str] = ..., files_present: bool = ..., file: _Optional[_Iterable[str]] = ..., exclude: _Optional[_Iterable[str]] = ..., symlink_behavior: _Optional[_Union[FilesetEntry.SymlinkBehavior, str]] = ..., strip_prefix: _Optional[str] = ...) -> None: ...

class GeneratedFile(_message.Message):
    __slots__ = ["generating_rule", "location", "name"]
    GENERATING_RULE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    generating_rule: str
    location: str
    name: str
    def __init__(self, name: _Optional[str] = ..., generating_rule: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class LabelDictUnaryEntry(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class LabelKeyedStringDictEntry(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class LabelListDictEntry(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...

class License(_message.Message):
    __slots__ = ["exception", "license_type"]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    exception: _containers.RepeatedScalarFieldContainer[str]
    license_type: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, license_type: _Optional[_Iterable[str]] = ..., exception: _Optional[_Iterable[str]] = ...) -> None: ...

class PackageGroup(_message.Message):
    __slots__ = ["contained_package", "included_package_group", "name"]
    CONTAINED_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_PACKAGE_GROUP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    contained_package: _containers.RepeatedScalarFieldContainer[str]
    included_package_group: _containers.RepeatedScalarFieldContainer[str]
    name: str
    def __init__(self, name: _Optional[str] = ..., contained_package: _Optional[_Iterable[str]] = ..., included_package_group: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ["target"]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: _containers.RepeatedCompositeFieldContainer[Target]
    def __init__(self, target: _Optional[_Iterable[_Union[Target, _Mapping]]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ["DEPRECATED_is_skylark", "DEPRECATED_public_by_default", "attribute", "configured_rule_input", "default_setting", "definition_stack", "instantiation_stack", "location", "name", "rule_class", "rule_input", "rule_output", "skylark_environment_hash_code"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_RULE_INPUT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SETTING_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_STACK_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_IS_SKYLARK_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PUBLIC_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_is_skylark: bool
    DEPRECATED_public_by_default: bool
    INSTANTIATION_STACK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_CLASS_FIELD_NUMBER: _ClassVar[int]
    RULE_INPUT_FIELD_NUMBER: _ClassVar[int]
    RULE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SKYLARK_ENVIRONMENT_HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    attribute: _containers.RepeatedCompositeFieldContainer[Attribute]
    configured_rule_input: _containers.RepeatedCompositeFieldContainer[ConfiguredRuleInput]
    default_setting: _containers.RepeatedScalarFieldContainer[str]
    definition_stack: _containers.RepeatedScalarFieldContainer[str]
    instantiation_stack: _containers.RepeatedScalarFieldContainer[str]
    location: str
    name: str
    rule_class: str
    rule_input: _containers.RepeatedScalarFieldContainer[str]
    rule_output: _containers.RepeatedScalarFieldContainer[str]
    skylark_environment_hash_code: str
    def __init__(self, name: _Optional[str] = ..., rule_class: _Optional[str] = ..., location: _Optional[str] = ..., attribute: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ..., rule_input: _Optional[_Iterable[str]] = ..., configured_rule_input: _Optional[_Iterable[_Union[ConfiguredRuleInput, _Mapping]]] = ..., rule_output: _Optional[_Iterable[str]] = ..., default_setting: _Optional[_Iterable[str]] = ..., DEPRECATED_public_by_default: bool = ..., DEPRECATED_is_skylark: bool = ..., skylark_environment_hash_code: _Optional[str] = ..., instantiation_stack: _Optional[_Iterable[str]] = ..., definition_stack: _Optional[_Iterable[str]] = ...) -> None: ...

class RuleDefinition(_message.Message):
    __slots__ = ["attribute", "documentation", "label", "name"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    attribute: _containers.RepeatedCompositeFieldContainer[AttributeDefinition]
    documentation: str
    label: str
    name: str
    def __init__(self, name: _Optional[str] = ..., attribute: _Optional[_Iterable[_Union[AttributeDefinition, _Mapping]]] = ..., documentation: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class RuleSummary(_message.Message):
    __slots__ = ["dependency", "location", "rule"]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    dependency: _containers.RepeatedCompositeFieldContainer[Rule]
    location: str
    rule: Rule
    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]] = ..., dependency: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ..., location: _Optional[str] = ...) -> None: ...

class SourceFile(_message.Message):
    __slots__ = ["feature", "license", "location", "name", "package_contains_errors", "package_group", "subinclude", "visibility_label"]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_CONTAINS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUBINCLUDE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_LABEL_FIELD_NUMBER: _ClassVar[int]
    feature: _containers.RepeatedScalarFieldContainer[str]
    license: License
    location: str
    name: str
    package_contains_errors: bool
    package_group: _containers.RepeatedScalarFieldContainer[str]
    subinclude: _containers.RepeatedScalarFieldContainer[str]
    visibility_label: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., location: _Optional[str] = ..., subinclude: _Optional[_Iterable[str]] = ..., package_group: _Optional[_Iterable[str]] = ..., visibility_label: _Optional[_Iterable[str]] = ..., feature: _Optional[_Iterable[str]] = ..., license: _Optional[_Union[License, _Mapping]] = ..., package_contains_errors: bool = ...) -> None: ...

class StringDictEntry(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class StringListDictEntry(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ["environment_group", "generated_file", "package_group", "rule", "source_file", "type"]
    class Discriminator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ENVIRONMENT_GROUP: Target.Discriminator
    ENVIRONMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    GENERATED_FILE: Target.Discriminator
    GENERATED_FILE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_GROUP: Target.Discriminator
    PACKAGE_GROUP_FIELD_NUMBER: _ClassVar[int]
    RULE: Target.Discriminator
    RULE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILE: Target.Discriminator
    SOURCE_FILE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    environment_group: EnvironmentGroup
    generated_file: GeneratedFile
    package_group: PackageGroup
    rule: Rule
    source_file: SourceFile
    type: Target.Discriminator
    def __init__(self, type: _Optional[_Union[Target.Discriminator, str]] = ..., rule: _Optional[_Union[Rule, _Mapping]] = ..., source_file: _Optional[_Union[SourceFile, _Mapping]] = ..., generated_file: _Optional[_Union[GeneratedFile, _Mapping]] = ..., package_group: _Optional[_Union[PackageGroup, _Mapping]] = ..., environment_group: _Optional[_Union[EnvironmentGroup, _Mapping]] = ...) -> None: ...
