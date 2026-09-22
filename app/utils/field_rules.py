# app/utils/field_rules.py
from typing import List, Optional
from app.models.schema.model_schema import ModelField, ModelSchema

def infer_dart_type(field_name: str) -> str:
    """根据字段名推断 Dart 类型"""
    int_keywords = ['id', 'ctime', 'score', 'time', 'count', 'num']
    if any(keyword in field_name.lower() for keyword in int_keywords):
        return 'int'
    return 'String'

def get_default_value(field_name: str, dart_type: str) -> Optional[str]:
    """返回默认值表达式，如果不需要默认值返回 None"""
    if dart_type == 'int':
        if 'id' in field_name.lower():
            return '-1'
        return '0'
    return None

def build_model_schema(class_name: str, field_names: List[str]) -> ModelSchema:
    """根据类名和字段名列表构建 ModelSchema"""
    fields = []
    for name in field_names:
        dart_type = infer_dart_type(name)
        default_value = get_default_value(name, dart_type)
        fields.append(ModelField(name=name, dart_type=dart_type, default_value=default_value))
    return ModelSchema(class_name=class_name, fields=fields)