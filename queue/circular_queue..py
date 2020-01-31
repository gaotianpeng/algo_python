from typing import Optional
from itertools import chain

class CircularQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity: int = capacity + 1
        self._head: int = 0
        self._tail: int = 0

    def enqueue(self, item: str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            return False

        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True


    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head+1) % self._capacity
            return item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head : self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))

if __name__ == "__main__":
    queue_test = CircularQueue(10)
    for i in range(10):
        queue_test.enqueue(str(i))
    print(queue_test)
    for _ in range(3):
        queue_test.dequeue()
    print(queue_test)
