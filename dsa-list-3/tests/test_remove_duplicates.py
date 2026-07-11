from src.my_node import MyNode
from src.remove_duplicates import remove_duplicates


def create_linked_list(values):
    if not values:
        return None

    head = MyNode(values[0])
    current = head

    for v in values[1:]:
        current.next = MyNode(v)
        current = current.next

    return head


def to_list(head):
    result = []
    current = head

    while current:
        result.append(current.value)
        current = current.next

    return result


def test_remove_duplicates_basic():
    head = create_linked_list([1, 2, 2, 3])
    new_head = remove_duplicates(head)
    assert to_list(new_head) == [1, 2, 3]


def test_all_duplicates():
    head = create_linked_list([1, 1, 1])
    new_head = remove_duplicates(head)
    assert to_list(new_head) == [1]


def test_no_duplicates():
    head = create_linked_list([1, 2, 3])
    new_head = remove_duplicates(head)
    assert to_list(new_head) == [1, 2, 3]


def test_empty():
    assert remove_duplicates(None) is None


def test_single():
    head = create_linked_list([5])
    new_head = remove_duplicates(head)
    assert to_list(new_head) == [5]


def test_non_consecutive_duplicates():
    head = create_linked_list([1, 2, 1, 3, 2])
    new_head = remove_duplicates(head)
    assert to_list(new_head) == [1, 2, 3]


def test_large():
    values = [1, 2, 3, 2, 4, 1, 5]
    head = create_linked_list(values)
    new_head = remove_duplicates(head)
    assert to_list(new_head) == [1, 2, 3, 4, 5]
