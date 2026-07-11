from src.exercicio_10 import greet_names


def test_greet_names():
    names = ["Ana", "João"]
    result = greet_names(names)
    assert result == ["Hello, Ana!", "Hello, João!"]
