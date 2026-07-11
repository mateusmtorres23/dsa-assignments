from src.my_array import MyArray
from src.reverse_array import reverse_array


def create_array(values):
    arr = MyArray()
    for val in values:
        arr.append(val)
    return arr


def to_list(arr):
    return [arr[i] for i in range(len(arr))]


def test_reverse_basic():
    arr = create_array([1, 2, 3])
    reverse_array(arr)
    assert to_list(arr) == [3, 2, 1]


def test_reverse_empty():
    arr = create_array([])
    reverse_array(arr)
    assert to_list(arr) == []


def test_reverse_single():
    arr = create_array([5])
    reverse_array(arr)
    assert to_list(arr) == [5]


def test_reverse_two_elements():
    arr = create_array([1, 2])
    reverse_array(arr)
    assert to_list(arr) == [2, 1]


def test_reverse_duplicates():
    arr = create_array([1, 2, 2, 3])
    reverse_array(arr)
    assert to_list(arr) == [3, 2, 2, 1]


def test_reverse_negative_numbers():
    arr = create_array([-1, -2, -3])
    reverse_array(arr)
    assert to_list(arr) == [-3, -2, -1]


def test_reverse_in_place():
    arr = create_array([1, 2, 3, 4])
    original_id = id(arr)
    reverse_array(arr)
    assert id(arr) == original_id


def test_reverse_large():
    values = list(range(100))
    arr = create_array(values)
    reverse_array(arr)
    assert to_list(arr) == list(reversed(values))
