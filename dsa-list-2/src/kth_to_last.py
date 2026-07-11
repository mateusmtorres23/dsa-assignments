from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    fast = head
    slow = head

    for _ in range(k):
        if fast is None: return -1
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next
    
    return slow.value if slow else -1