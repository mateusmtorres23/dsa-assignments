from src.exercicio_16 import odd_numbers


def test_odd_numbers():
    assert odd_numbers(7) == [1, 3, 5, 7]
    assert odd_numbers(1) == [1]
