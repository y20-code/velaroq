from typing import List, Tuple

def parse_model_input(text: str) -> Tuple[str, List[str]]:
    """
        解析用户输入，返回类名和字段名列表。

        预期输入格式：
        第一行：类名
        后续行：字段名（每行一个）
    """
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    if not lines:
        raise ValueError("输入不能为空")

    class_name = lines[0]
    field_names = lines[1:]
    return class_name, field_names