from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1: 
        return array
    
    mid = len(array)//2

    left = MyArray()
    right = MyArray()

    for i in range(mid):
        left.append(array[i])
    for i in range(mid, len(array)):
        right.append(array[i])

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left:MyArray, right:MyArray) -> MyArray:
    arr = MyArray()
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    while i < len(left):
        arr.append(left[i])
        i+=1
    while j < len(right):
        arr.append(right[j])
        j+=1

    return arr