class MyArray:
    def __init__(self) -> None:
        self.data: list[int] = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def remove(self, value: int) -> None:
        for i in range(len(self.data)):
            if self.data[i] == value:
                for j in range(i, len(self.data) - 1):
                    self.data[j] = self.data[j + 1]
                self.data.pop()
                return
        raise ValueError("Value not found")

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")

        self.data.append(0)

        for i in range(len(self.data) - 1, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.set(index, value)

    def __repr__(self) -> str:
        return str(self.data)
