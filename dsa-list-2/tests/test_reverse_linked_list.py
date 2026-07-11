from src.my_node import MyNode
from src.reverse_linked_list import reverse_linked_list


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


def test_reverse_basic():
    head = create_linked_list([1, 2, 3])
    new_head = reverse_linked_list(head)
    assert to_list(new_head) == [3, 2, 1]


def test_reverse_empty():
    head = None
    new_head = reverse_linked_list(head)
    assert new_head is None


def test_reverse_single():
    head = create_linked_list([5])
    new_head = reverse_linked_list(head)
    assert to_list(new_head) == [5]


def test_reverse_two():
    head = create_linked_list([1, 2])
    new_head = reverse_linked_list(head)
    assert to_list(new_head) == [2, 1]


def test_reverse_large():
    values = list(range(10))
    head = create_linked_list(values)
    new_head = reverse_linked_list(head)
    assert to_list(new_head) == list(reversed(values))


def test_reverse_duplicates():
    head = create_linked_list([1, 2, 2, 3])
    new_head = reverse_linked_list(head)
    assert to_list(new_head) == [3, 2, 2, 1]


def test_reverse_negative():
    head = create_linked_list([-1, -2, -3])
    new_head = reverse_linked_list(head)
    assert to_list(new_head) == [-3, -2, -1]


def test_no_cycle_created():
    head = create_linked_list([1, 2, 3, 4])
    new_head = reverse_linked_list(head)

    visited = set()
    current = new_head

    while current:
        assert id(current) not in visited
        visited.add(id(current))
        current = current.next


def test_same_nodes_reused():
    head = create_linked_list([1, 2, 3])

    original_nodes = []
    current = head
    while current:
        original_nodes.append(current)
        current = current.next

    new_head = reverse_linked_list(head)

    reversed_nodes = []
    current = new_head
    while current:
        reversed_nodes.append(current)
        current = current.next

    assert set(original_nodes) == set(reversed_nodes)
