from src.my_array import MyArray
from src.quick_sort import quick_sort


def create_array(values):
    arr = MyArray()
    for v in values:
        arr.append(v)
    return arr


def to_list(arr):
    return [arr[i] for i in range(len(arr))]


def test_quick_sort_basic():
    arr = create_array([3, 1, 2])
    result = quick_sort(arr)
    assert to_list(result) == [1, 2, 3]


def test_sorted():
    arr = create_array([1, 2, 3, 4])
    result = quick_sort(arr)
    assert to_list(result) == [1, 2, 3, 4]


def test_reverse():
    arr = create_array([5, 4, 3, 2, 1])
    result = quick_sort(arr)
    assert to_list(result) == [1, 2, 3, 4, 5]


def test_duplicates():
    arr = create_array([3, 1, 2, 1])
    result = quick_sort(arr)
    assert to_list(result) == [1, 1, 2, 3]


def test_negative():
    arr = create_array([-1, -3, -2])
    result = quick_sort(arr)
    assert to_list(result) == [-3, -2, -1]


def test_empty():
    arr = create_array([])
    result = quick_sort(arr)
    assert to_list(result) == []


def test_single():
    arr = create_array([10])
    result = quick_sort(arr)
    assert to_list(result) == [10]


def test_large():
    values = list(range(50, 0, -1))
    arr = create_array(values)
    result = quick_sort(arr)
    assert to_list(result) == sorted(values)
