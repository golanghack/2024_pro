#! /usr/bin/env python3

from typing import Any
from LinkedList import LinkedList


class LinkedQueue:
    """Create Queue with linked list
    
    :enqueue:       -> added element in queue
    :dequeue:       -> remove element from queue
    :peek:          -> return element from start position
    :len:           -> return lenght queue
    :isempty:       -> is empty queue test
    """

    def __init__(self) -> None:
        self._list = LinkedList()

    def enqueue(self, item: Any) -> None:
        """Added element in queue"""

        self._list.add_first(item)

    def dequeue(self) -> Any:
        """Remove first element"""

        return self._list.remove_first()

    def peek(self) -> Any:
        """Remove a first element"""

        item = self._list.remove_first()
        self._list.add_first(item)
        return item

    def __len__(self) -> int:
        """Lenght of queue"""

        return len(self._list)

    def is_empty(self) -> int:
        """is empty of queue"""

        return len(self) == 0
