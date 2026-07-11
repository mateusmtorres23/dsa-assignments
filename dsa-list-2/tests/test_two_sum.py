from src.my_array import MyArray
from src.two_sum import two_sum


def create_array(values):
    arr = MyArray()
    for v in values:
        arr.append(v)
    return arr


def test_two_sum_basic():
    arr = create_array([2, 7, 11, 15])
    assert two_sum(arr, 9) == (0, 1)


def test_two_sum_second_case():
    arr = create_array([3, 2, 4])
    assert two_sum(arr, 6) == (1, 2)


def test_two_sum_no_solution():
    arr = create_array([1, 2, 3])
    assert two_sum(arr, 7) == (-1, -1)


def test_two_sum_duplicates():
    arr = create_array([3, 3])
    assert two_sum(arr, 6) == (0, 1)


def test_two_sum_negative_numbers():
    arr = create_array([-1, -2, -3, -4])
    assert two_sum(arr, -6) == (1, 3)


def test_two_sum_empty():
    arr = create_array([])
    assert two_sum(arr, 5) == (-1, -1)


def test_two_sum_single():
    arr = create_array([10])
    assert two_sum(arr, 10) == (-1, -1)
