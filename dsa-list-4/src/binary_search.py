from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = array.get(mid)

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
