from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i]+array[j] == target:
                return (i, j)
    return (-1, -1)
