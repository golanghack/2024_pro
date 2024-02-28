#! /usr/bin/env python3

from typing import Any


class ListQueueFakeDelete:
    """Realisation queue with list data of python
    
    :enqueue:       -> added new element in queue
    :dequeue:       -> delete element from queue
    :peek:          -> return first element from queue
    :isempty:       -> is empty queue
    :len:           -> lenght queue
    """

    def __init__(self) -> None:
        self._head = 0
        self._list = []

    def enqueue(self, item: Any) -> None:
        """Added new element in queue"""

        self._list.append(item)

    def peek(self) -> Any:
        """Return a first element from queue"""

        return self._list[self._head]

    def dequeue(self) -> Any:
        """Remove element from queue and return"""

        item = self.peek()
        self._head += 1
        return item

    def isempty(self) -> bool:
        """Is empty?"""

        return len(self) == 0

    def __len__(self) -> int:
        """Return lenght of queue"""

        return len(self._list) - self._head
