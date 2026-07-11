import pytest
from src.my_array import MyArray


def test_starts_empty():
    arr = MyArray()
    assert len(arr) == 0


def test_append_increases_size():
    arr = MyArray()

    arr.append(1)
    arr.append(2)

    assert len(arr) == 2


def test_get_returns_correct_value():
    arr = MyArray()
    arr.append(10)

    assert arr.get(0) == 10


def test_getitem_returns_correct_value():
    arr = MyArray()
    arr.append(20)

    assert arr[0] == 20


def test_get_invalid_index_raises():
    arr = MyArray()

    with pytest.raises(IndexError):
        arr.get(0)


def test_getitem_invalid_index_raises():
    arr = MyArray()

    with pytest.raises(IndexError):
        _ = arr[0]


def test_set_updates_value():
    arr = MyArray()
    arr.append(1)

    arr.set(0, 5)

    assert arr.get(0) == 5


def test_setitem_updates_value():
    arr = MyArray()
    arr.append(2)

    arr[0] = 7

    assert arr[0] == 7


def test_set_invalid_index_raises():
    arr = MyArray()

    with pytest.raises(IndexError):
        arr.set(0, 1)


def test_setitem_invalid_index_raises():
    arr = MyArray()

    with pytest.raises(IndexError):
        arr[0] = 1


def test_insert_at_beginning():
    arr = MyArray()

    arr.append(2)
    arr.insert(0, 1)

    assert arr[0] == 1
    assert arr[1] == 2


def test_insert_in_middle():
    arr = MyArray()

    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)

    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3


def test_insert_at_end():
    arr = MyArray()

    arr.append(1)
    arr.insert(1, 2)

    assert arr[1] == 2


def test_insert_invalid_index_raises():
    arr = MyArray()

    with pytest.raises(IndexError):
        arr.insert(1, 10)


def test_remove_existing_value():
    arr = MyArray()

    arr.append(1)
    arr.append(2)
    arr.append(3)

    arr.remove(2)

    assert len(arr) == 2
    assert arr[1] == 3


def test_remove_first_occurrence_only():
    arr = MyArray()

    arr.append(1)
    arr.append(2)
    arr.append(2)
    arr.append(3)

    arr.remove(2)

    assert len(arr) == 3
    assert arr[1] == 2


def test_remove_value_not_found_raises():
    arr = MyArray()

    arr.append(1)

    with pytest.raises(ValueError):
        arr.remove(99)


def test_repr_empty():
    arr = MyArray()

    assert repr(arr) == "[]"


def test_repr_with_values():
    arr = MyArray()

    arr.append(1)
    arr.append(2)

    assert repr(arr) == "[1, 2]"


def test_sequence_of_operations():
    arr = MyArray()

    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)

    arr[0] = 10
    arr.remove(2)

    assert len(arr) == 2
    assert arr[0] == 10
    assert arr[1] == 3
