from src.node import Node


def test_node_initialization():
    node = Node(10)

    assert node.value == 10
    assert node.next is None


def test_node_linking():
    n1 = Node(1)
    n2 = Node(2)

    n1.next = n2

    assert n1.next == n2
    assert n1.next.value == 2
