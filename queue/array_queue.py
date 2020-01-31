from typing import Optional

class ArrayQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity:int = capacity
        self._head:int = 0
        self._tail:int = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range (0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            None

    def print_all(self):
            print(self._items[self._head: self._tail-1])

if __name__ == "__main__":
    queue_test = ArrayQueue(20)

    for i in range(10):
        queue_test.enqueue(str(i))
    queue_test.print_all()

    for i in range(5):
        queue_test.dequeue()
    queue_test.print_all()

