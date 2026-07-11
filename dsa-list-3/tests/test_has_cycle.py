from src.my_node import MyNode
from src.has_cycle import has_cycle


def create_linked_list(values):
    if not values:
        return None

    head = MyNode(values[0])
    current = head

    nodes = [head]

    for v in values[1:]:
        new_node = MyNode(v)
        current.next = new_node
        current = new_node
        nodes.append(new_node)

    return head, nodes


def test_no_cycle():
    head, _ = create_linked_list([1, 2, 3])
    assert has_cycle(head) is False


def test_empty():
    assert has_cycle(None) is False


def test_single_no_cycle():
    head = MyNode(1)
    assert has_cycle(head) is False


def test_single_with_cycle():
    head = MyNode(1)
    head.next = head
    assert has_cycle(head) is True


def test_cycle_middle():
    head, nodes = create_linked_list([1, 2, 3, 4])
    nodes[-1].next = nodes[1]
    assert has_cycle(head) is True


def test_cycle_at_start():
    head, nodes = create_linked_list([1, 2, 3])
    nodes[-1].next = head
    assert has_cycle(head) is True


def test_large_no_cycle():
    head, _ = create_linked_list(list(range(50)))
    assert has_cycle(head) is False


def test_large_with_cycle():
    head, nodes = create_linked_list(list(range(50)))
    nodes[-1].next = nodes[10]
    assert has_cycle(head) is True
