from src.my_array import MyArray


def linear_search(array: MyArray, target: int) -> int:
    for i in range(len(array)):
        if array.get(i) == target:
            return i
    return -1
