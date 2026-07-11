from src.my_node import MyNode
from src.merge_lists import merge_lists


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


def test_merge_basic():
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    merged = merge_lists(l1, l2)
    assert to_list(merged) == [1, 2, 3, 4, 5, 6]


def test_different_sizes():
    l1 = create_linked_list([1, 2])
    l2 = create_linked_list([3, 4, 5])
    merged = merge_lists(l1, l2)
    assert to_list(merged) == [1, 2, 3, 4, 5]


def test_one_empty():
    l1 = create_linked_list([])
    l2 = create_linked_list([1, 2, 3])
    merged = merge_lists(l1, l2)
    assert to_list(merged) == [1, 2, 3]


def test_both_empty():
    assert merge_lists(None, None) is None


def test_with_duplicates():
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([1, 3, 5])
    merged = merge_lists(l1, l2)
    assert to_list(merged) == [1, 1, 3, 3, 5, 5]


def test_large():
    l1 = create_linked_list(list(range(0, 20, 2)))
    l2 = create_linked_list(list(range(1, 20, 2)))
    merged = merge_lists(l1, l2)
    assert to_list(merged) == list(range(20))


def test_reuse_nodes():
    l1 = create_linked_list([1, 3])
    l2 = create_linked_list([2, 4])

    original_nodes = set()

    current = l1
    while current:
        original_nodes.add(id(current))
        current = current.next

    current = l2
    while current:
        original_nodes.add(id(current))
        current = current.next

    merged = merge_lists(l1, l2)

    merged_nodes = set()
    current = merged
    while current:
        merged_nodes.add(id(current))
        current = current.next

    assert merged_nodes == original_nodes
