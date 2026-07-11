from src.my_array import MyArray
from src.linear_search import linear_search


def test_linear_search_found():
    arr = MyArray()

    arr.append(10)
    arr.append(20)
    arr.append(30)

    assert linear_search(arr, 20) == 1


def test_linear_search_not_found():
    arr = MyArray()

    arr.append(1)
    arr.append(2)

    assert linear_search(arr, 99) == -1


def test_linear_search_empty_array():
    arr = MyArray()

    assert linear_search(arr, 10) == -1


def test_linear_search_single_element_found():
    arr = MyArray()

    arr.append(5)

    assert linear_search(arr, 5) == 0


def test_linear_search_single_element_not_found():
    arr = MyArray()

    arr.append(5)

    assert linear_search(arr, 10) == -1


def test_linear_search_first_element():
    arr = MyArray()

    arr.append(5)
    arr.append(10)
    arr.append(15)

    assert linear_search(arr, 5) == 0


def test_linear_search_last_element():
    arr = MyArray()

    arr.append(5)
    arr.append(10)
    arr.append(15)

    assert linear_search(arr, 15) == 2


def test_linear_search_returns_first_occurrence():
    arr = MyArray()

    arr.append(1)
    arr.append(2)
    arr.append(2)
    arr.append(3)

    assert linear_search(arr, 2) == 1
