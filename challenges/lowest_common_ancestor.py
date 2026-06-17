from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    
    if root is None or root.value is None:
        return -1

    if root.value > value1 and root.value > value2:
        return lowest_common_ancestor(root.get_left_child(), value1, value2)
    
    elif root.value < value1 and root.value < value2:
        return lowest_common_ancestor(root.get_right_child(), value1, value2)
    
    else:
        return root.value
