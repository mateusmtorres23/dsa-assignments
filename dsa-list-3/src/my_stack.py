class MyStack:
    def __init__(self) -> None:
        self.data = []

    def size(self) -> int:
        return len(self.data)

    def is_empty(self) -> bool:
        return not bool(self.size())

    def push(self, value) -> None:
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]
