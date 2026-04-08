from src.array import Array


class MyArray(Array):
    """
    Implementação concreta do TAD Array.
    """

    def __init__(self) -> None:
        self.data: list[int] = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def get(self, index: int) -> int:
        return self.data[index]

    def set(self, index: int, value: int) -> None:
        self.data[index] = value

    def remove(self, value: int) -> None:
        self.data.remove(value)

    def insert(self, index: int, value: int) -> None:
        self.data.insert(index, value)

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> int:
        return self.data[index]

    def __setitem__(self, index: int, value: int) -> None:
        self.data[index] = value

    def __repr__(self) -> str:
        return f"MyArray({self.data})"
