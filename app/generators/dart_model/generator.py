# app/generators/dart_model/generator.py
import os
from jinja2 import Environment, FileSystemLoader
from app.models.schema.model_schema import ModelSchema


def generate_model_code(schema: ModelSchema) -> str:
    """
    使用 Jinja2 模板渲染 Dart Model 代码。

    Args:
        schema: 描述 Dart Model 的 ModelSchema 实例。

    Returns:
        生成的 Dart 代码字符串。
    """
    # 模板目录：项目根目录下的 templates/flutter/model
    template_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
        'templates',
        'flutter',
        'model'
    )

    # 创建 Jinja2 环境并加载模板
    env = Environment(loader=FileSystemLoader(template_dir),trim_blocks=True,lstrip_blocks=True)
    template = env.get_template('dart_model.j2')

    # 渲染模板，传入 schema 变量
    rendered = template.render(schema=schema)
    return rendered