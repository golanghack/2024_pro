#! /usr/bin/env python3

from typing import Any
from ListQueueFakeDelete import ListQueueFakeDelete


class ListQueueWithFakeDelete(ListQueueFakeDelete):
    """ 
    Realistion queue with delegate fake delete queue"""

    def dequeue(self) -> Any:
        item = self._list[self._head]
        self._head += 1
        if self._head > len(self._list) // 2:
            self._list = self._list[self._head :]
            self._head = 0
        return item
