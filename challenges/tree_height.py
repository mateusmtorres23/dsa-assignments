from data_structures.node import Node


def tree_height(root: Node | None) -> int:
    if root is None:
        return -1

    return 1 + max(
        tree_height(root.get_left_child()), tree_height(root.get_right_child())
        )
