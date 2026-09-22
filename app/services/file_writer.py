# app/services/file_writer.py
import os


def write_dart_file(content: str, output_path: str) -> None:
    """
    将内容写入指定的 .dart 文件。

    Args:
        content: 要写入的字符串。
        output_path: 目标文件路径，例如 './output/DailySentenceComDataEntity.dart'。

    Raises:
        IOError: 如果写入失败（如目录不存在或权限不足）。
    """
    # 确保输出目录存在
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"无法写入文件 {output_path}: {e}")