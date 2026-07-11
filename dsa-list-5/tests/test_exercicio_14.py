from src.exercicio_14 import generate_numbers


def test_generate_numbers():
    assert generate_numbers(5) == [1, 2, 3, 4, 5]
    assert generate_numbers(0) == []
    assert generate_numbers(1) == [1]
