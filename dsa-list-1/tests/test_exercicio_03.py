from src.exercicio_03 import personal_message


def test_personal_message():
    assert personal_message("Carlos") == "Hello, Carlos!"
    assert personal_message("Ana") == "Hello, Ana!"
