from src.my_array import MyArray
from src.merge_sort import merge_sort


def create_array(values):
    arr = MyArray()
    for v in values:
        arr.append(v)
    return arr


def to_list(arr):
    return [arr[i] for i in range(len(arr))]


def test_merge_sort_basic():
    arr = create_array([3, 1, 2])
    result = merge_sort(arr)
    assert to_list(result) == [1, 2, 3]


def test_already_sorted():
    arr = create_array([1, 2, 3, 4])
    result = merge_sort(arr)
    assert to_list(result) == [1, 2, 3, 4]


def test_reverse_order():
    arr = create_array([5, 4, 3, 2, 1])
    result = merge_sort(arr)
    assert to_list(result) == [1, 2, 3, 4, 5]


def test_duplicates():
    arr = create_array([3, 1, 2, 1])
    result = merge_sort(arr)
    assert to_list(result) == [1, 1, 2, 3]


def test_negative_numbers():
    arr = create_array([-1, -3, -2])
    result = merge_sort(arr)
    assert to_list(result) == [-3, -2, -1]


def test_empty():
    arr = create_array([])
    result = merge_sort(arr)
    assert to_list(result) == []


def test_single():
    arr = create_array([10])
    result = merge_sort(arr)
    assert to_list(result) == [10]


def test_large():
    values = list(range(50, 0, -1))
    arr = create_array(values)
    result = merge_sort(arr)
    assert to_list(result) == sorted(values)
