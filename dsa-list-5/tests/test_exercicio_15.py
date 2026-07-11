from src.exercicio_15 import sum_numbers


def test_sum_numbers():
    assert sum_numbers(5) == 15
    assert sum_numbers(1) == 1
    assert sum_numbers(2) == 3
