# tests/test_input_parser.py
from app.utils.input_parser import parse_model_input


def test_parse_model_input_basic():
    text = """DailySentenceComDataEntity
id
userId
score
voice
"""
    class_name, fields = parse_model_input(text)
    assert class_name == "DailySentenceComDataEntity"
    assert fields == ["id", "userId", "score", "voice"]


def test_parse_model_input_ignore_blank_lines():
    text = """

    DailySentenceComDataEntity

    id

    userId

    """
    class_name, fields = parse_model_input(text)
    assert class_name == "DailySentenceComDataEntity"
    assert fields == ["id", "userId"]


def test_parse_model_input_empty_raises_error():
    import pytest
    with pytest.raises(ValueError):
        parse_model_input("   \n  \n")