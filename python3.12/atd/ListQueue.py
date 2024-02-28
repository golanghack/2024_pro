#! /usr/bin/env python3

from typing import Any


class ListQueueSimple:
    """Realisation queue a a FIFO with list
    
    :enqueue:       -> added new element
    :dequeue:       -> delete and return of element
    :peek:          -> FIFO ordered return element
    :__len__:       -> return lenght of queue
    :isempty:       -> return boolean mean for empty/noempty queue
    """

    def __init__(self):
        self._list = []

    def enqueue(self, item: Any) -> None:
        """Added element in queue"""
        self._list.append(item)

    def dequeue(self) -> Any:
        """Remove element from queue"""

        return self._list.pop(0)

    def peek(self) -> Any:
        """Return zero element from queue"""

        return self._list[0]

    def isempty(self) -> bool:
        """Is empty?"""

        return len(self) == 0

    def __len__(self) -> int:
        """Return lenght of queue"""

        return len(self._list)
