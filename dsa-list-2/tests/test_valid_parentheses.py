from src.valid_parentheses import is_valid_parentheses


def test_valid_simple():
    assert is_valid_parentheses("()") is True


def test_valid_multiple_types():
    assert is_valid_parentheses("()[]{}") is True


def test_valid_nested():
    assert is_valid_parentheses("{[]}") is True


def test_invalid_simple():
    assert is_valid_parentheses("(]") is False


def test_invalid_order():
    assert is_valid_parentheses("([)]") is False


def test_only_open():
    assert is_valid_parentheses("(((") is False


def test_only_close():
    assert is_valid_parentheses(")))") is False


def test_empty_string():
    assert is_valid_parentheses("") is True


def test_large_valid():
    s = "({[]})" * 10
    assert is_valid_parentheses(s) is True
