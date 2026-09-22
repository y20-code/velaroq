# manual_test.py（放在项目根目录）
from app.utils.input_parser import parse_model_input
from app.utils.field_rules import build_model_schema
from app.generators.dart_model.generator import generate_model_code
from app.services.file_writer import write_dart_file

user_input = """DailySentenceComDataEntity
id
userId
sourceId
score
voice
ctime
"""

class_name, field_names = parse_model_input(user_input)
schema = build_model_schema(class_name, field_names)
dart_code = generate_model_code(schema)

print(dart_code)  # 仍然打印预览

# 输出到当前目录下的 output 文件夹
output_file = "output/DailySentenceComDataEntity.dart"
write_dart_file(dart_code, output_file)
print(f"已生成文件: {output_file}")