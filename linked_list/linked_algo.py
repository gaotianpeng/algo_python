import sys
sys.path.append("single_linked_list")

from single_linked_list import SinglyLinkedList
from single_linked_list import Node

def reverse(head):
    # print(head.data)
    p = None
    q = None
    while head:
        # print(head.data)
        q = head._next
        head = q._next
        q = head
        p = q
    return p

if __name__ == '__main__':
    single_l = SinglyLinkedList()
    for i in range(20):
        single_l.insert_value_to_head(i)
