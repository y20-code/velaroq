# tests/test_model_schema.py
from app.models.schema.model_schema import ModelField, ModelSchema

def test_create_model_field():
    field = ModelField(name="userId", dart_type="int", default_value="-1")
    assert field.name == "userId"
    assert field.dart_type == "int"
    assert field.default_value == "-1"

def test_create_model_schema():
    field1 = ModelField(name="id", dart_type="int", default_value="-1")
    field2 = ModelField(name="voice", dart_type="String")
    schema = ModelSchema(class_name="TestModel", fields=[field1, field2])
    assert schema.class_name == "TestModel"
    assert len(schema.fields) == 2
    assert schema.fields[1].dart_type == "String"
    assert schema.fields[1].default_value is None