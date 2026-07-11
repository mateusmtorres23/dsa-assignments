from data_structures.node import Node


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        if new_node.get_value() == node.get_value():
            return 0

        elif new_node.get_value() < node.get_value():
            return -1

        else:
            return 1

    def insert_with_recursion(self, value):

        if self.get_root() is None:
            self.set_root(value)
            return

        self.insert_recursively(self.get_root(), Node(value))

    def insert_recursively(self, node, new_node):

        comparison = self.compare(node, new_node)

        if comparison == 0:
            node.set_value(new_node.get_value())

        elif comparison == -1:

            if node.has_left_child():
                self.insert_recursively(
                    node.get_left_child(),
                    new_node
                )
            else:
                node.set_left_child(new_node)

        else:

            if node.has_right_child():
                self.insert_recursively(
                    node.get_right_child(),
                    new_node
                )
            else:
                node.set_right_child(new_node)

    def delete(self, value):
        self.root = self.delete_recursively(self.root, value)

    def delete_recursively(self, node, value):
        if node is None:
            return None

        if value < node.get_value():

            node.set_left_child(
                self.delete_recursively(
                    node.get_left_child(),
                    value
                )
            )

        elif value > node.get_value():

            node.set_right_child(
                self.delete_recursively(
                    node.get_right_child(),
                    value
                )
            )

        else:

            if (
                not node.has_left_child()
                and
                not node.has_right_child()
            ):
                return None

            elif not node.has_left_child():
                return node.get_right_child()

            elif not node.has_right_child():
                return node.get_left_child()

            else:
                successor = self.get_min(node.get_right_child())

                node.set_value(successor.get_value())

                node.set_right_child(
                    self.delete_recursively(
                        node.get_right_child(),
                        successor.get_value()
                    )
                )

        return node

    def get_min(self, node):
        current = node

        while current.has_left_child():
            current = current.get_left_child()

        return current
