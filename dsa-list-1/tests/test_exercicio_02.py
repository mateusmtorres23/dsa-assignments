from src.exercicio_02 import simple_message


def test_simple_message():
    assert simple_message("Python") == "Python"
    assert simple_message("12345") == "12345"
    assert simple_message("") == ""
