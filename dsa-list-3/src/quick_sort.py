from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    pivot = array[len(array) - 1]

    left = MyArray()
    right = MyArray()

    for i in range(len(array) - 1):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    arr = MyArray()

    for i in range(len(left_sorted)):
        arr.append(left_sorted[i])

    arr.append(pivot)

    for i in range(len(right_sorted)):
        arr.append(right_sorted[i])
    
    return arr
