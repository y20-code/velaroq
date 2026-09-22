from dataclasses import dataclass, field
from typing import List,Optional

@dataclass
class ModelField:
    """描述一个 Dart Model 字段"""
    name: str                      # 字段名，驼峰命名，如 userId
    dart_type: str                 # Dart 类型，如 int, String
    default_value: Optional[str] = None  # fromJson 中 ?? 后面的默认值表达式，如 "-1"、"0"，None 表示不需要默认值

@dataclass
class ModelSchema:
    """描述一个完整的 Dart Model"""
    class_name: str
    fields: List[ModelField] = field(default_factory=list)