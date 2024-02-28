#! /usr/bin/env python3

from typing import Any
from ListNode import ListNode


class LinkedList:
    """Linked list realisation with python
    
    :add_first:         -> add element in head
    :remove_first:      -> delete element from head
    """

    def __init__(self) -> None:
        self._head = None

    def add_first(self, item: Any) -> None:
        """Adde item in first positions"""

        self._head = ListNode(item, self._head)

    def remove_first(self) -> Any:
        """Remove first element"""

        item = self._head.data
        self._head = self._head.link
        return item
