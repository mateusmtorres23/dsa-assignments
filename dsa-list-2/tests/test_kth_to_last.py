from src.my_node import MyNode
from src.kth_to_last import kth_to_last


def create_linked_list(values):
    if not values:
        return None

    head = MyNode(values[0])
    current = head

    for v in values[1:]:
        current.next = MyNode(v)
        current = current.next

    return head


def test_kth_basic():
    head = create_linked_list([1, 2, 3, 4, 5])
    assert kth_to_last(head, 1) == 5
    assert kth_to_last(head, 2) == 4
    assert kth_to_last(head, 5) == 1


def test_k_greater_than_length():
    head = create_linked_list([1, 2, 3])
    assert kth_to_last(head, 4) == -1


def test_single_element():
    head = create_linked_list([10])
    assert kth_to_last(head, 1) == 10
    assert kth_to_last(head, 2) == -1


def test_empty():
    assert kth_to_last(None, 1) == -1


def test_k_zero():
    head = create_linked_list([1, 2, 3])
    assert kth_to_last(head, 0) == -1


def test_large():
    values = list(range(1, 21))
    head = create_linked_list(values)
    assert kth_to_last(head, 1) == 20
    assert kth_to_last(head, 10) == 11
