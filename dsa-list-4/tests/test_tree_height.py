from challenges.tree_height import tree_height

from data_structures.tree import Tree


def test_empty_tree():
    assert tree_height(None) == -1


def test_tree_with_root_only():
    tree = Tree()

    tree.insert_with_recursion(10)

    assert tree_height(
        tree.get_root()
    ) == 0


def test_two_levels():
    tree = Tree()

    tree.insert_with_recursion(10)
    tree.insert_with_recursion(5)

    assert tree_height(
        tree.get_root()
    ) == 1


def test_three_levels_left():
    tree = Tree()

    tree.insert_with_recursion(10)
    tree.insert_with_recursion(5)
    tree.insert_with_recursion(2)

    assert tree_height(
        tree.get_root()
    ) == 2


def test_three_levels_right():
    tree = Tree()

    tree.insert_with_recursion(10)
    tree.insert_with_recursion(15)
    tree.insert_with_recursion(20)

    assert tree_height(
        tree.get_root()
    ) == 2


def test_balanced_tree():
    tree = Tree()

    for value in [
        4,
        2,
        6,
        1,
        3,
        5,
        7,
    ]:
        tree.insert_with_recursion(value)

    assert tree_height(
        tree.get_root()
    ) == 2


def test_unbalanced_tree():
    tree = Tree()

    for value in [
        1,
        2,
        3,
        4,
        5,
    ]:
        tree.insert_with_recursion(value)

    assert tree_height(
        tree.get_root()
    ) == 4


def test_height_follows_longest_path():
    tree = Tree()

    for value in [
        10,
        5,
        20,
        2,
        1,
    ]:
        tree.insert_with_recursion(value)

    assert tree_height(
        tree.get_root()
    ) == 3


def test_height_after_leaf_deletion():
    tree = Tree()

    for value in [
        4,
        2,
        6,
        1,
        3,
        5,
        7,
    ]:
        tree.insert_with_recursion(value)

    tree.delete(7)

    assert tree_height(
        tree.get_root()
    ) == 2


def test_height_after_deepest_node_deletion():
    tree = Tree()

    for value in [
        1,
        2,
        3,
        4,
        5,
    ]:
        tree.insert_with_recursion(value)

    tree.delete(5)

    assert tree_height(
        tree.get_root()
    ) == 3


def test_duplicate_insertions_do_not_change_height():
    tree = Tree()

    tree.insert_with_recursion(10)
    tree.insert_with_recursion(5)
    tree.insert_with_recursion(15)

    original_height = tree_height(
        tree.get_root()
    )

    tree.insert_with_recursion(10)
    tree.insert_with_recursion(5)
    tree.insert_with_recursion(15)

    assert tree_height(
        tree.get_root()
    ) == original_height
