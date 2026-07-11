from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    current = head

    while current is not None:
        last_unique = current
        check = current.next

        while check is not None:
            if check.value == current.value:
                last_unique.next = check.next
                check = check.next
                continue
            
            last_unique = check
            check = check.next

        current = current.next

    return head
