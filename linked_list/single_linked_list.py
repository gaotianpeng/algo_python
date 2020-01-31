from typing import Optional

class Node(object):
    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node

class SinglyLinkedList(object):
    def __init__(self):
        self._head = None

    def get_head(self) -> Optional[Node]:
        if self._head is not None:
            return self._head
        return None

    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and  p.data != value:
            p = p.next
        return p

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node is not None:
            new_node._next = self._head
            self._head = new_node

    def dump_link_list(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current._next
        while current:
            print(f"->{current.data}", end="")
            current = current._next
        print("\n", flush=True)

    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    def delete_by_node(self, node: Node):
        if not self._head or not node:
            return
        if node._next:
            node.data = node._next.data
            node._next = node._next._next
            return
        # node is the last one or not in the list
        current = self._head
        while current and current._next != node:
            current = current._next
        if not current:
            return
        current._next = node._next

    def delete_by_value(self, value: int):
        if not self._head or not value:
            return
        fake_head = Node(value + 1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:
            prev._next = None
        self._head = fake_head._next  # in case head.data == value

if __name__ == "__main__":
    single_l = SinglyLinkedList()
    for i in range(20):
        single_l.insert_value_to_head(i)

    single_l.dump_link_list()
    print(single_l.find_by_value(9).data)
    print('delete 10, 11, 12')
    single_l.delete_by_value(10)
    single_l.delete_by_value(11)
    single_l.delete_by_value(12)
    single_l.dump_link_list()


