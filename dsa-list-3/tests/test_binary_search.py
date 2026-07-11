from src.my_array import MyArray
from src.binary_search import binary_search


def test_binary_search_found():
    arr = MyArray()

    arr.append(1)
    arr.append(3)
    arr.append(5)
    arr.append(7)

    assert binary_search(arr, 5) == 2


def test_binary_search_not_found():
    arr = MyArray()

    arr.append(1)
    arr.append(3)
    arr.append(5)

    assert binary_search(arr, 2) == -1


def test_binary_search_first_element():
    arr = MyArray()

    arr.append(1)
    arr.append(3)
    arr.append(5)

    assert binary_search(arr, 1) == 0


def test_binary_search_last_element():
    arr = MyArray()

    arr.append(1)
    arr.append(3)
    arr.append(5)

    assert binary_search(arr, 5) == 2


def test_binary_search_single_element():
    arr = MyArray()

    arr.append(10)

    assert binary_search(arr, 10) == 0


def test_binary_search_empty():
    arr = MyArray()

    assert binary_search(arr, 10) == -1
