from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    temp_head = MyNode(0)
    tail = temp_head

    while lista1 is not None and lista2 is not None:
        if lista1.value < lista2.value:
            tail.next = lista1
            lista1 = lista1.next
        else:
            tail.next = lista2
            lista2 = lista2.next

        tail = tail.next
    
    if lista1 is not None:
        tail.next = lista1
    elif lista2 is not None:
        tail.next = lista2

    return temp_head.next
    



