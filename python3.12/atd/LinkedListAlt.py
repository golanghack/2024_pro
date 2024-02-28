#! /usr/bin/env python3

from typing import Any
from ListNode import ListNode


class LinkedListAlt:
    """Create Linked list on python
    
    :add_first:         -> add first element 
    :add_last:          -> add last element
    :remove_first:      -> remove first element
    :remove_last:       -> remove last element
    :__len__:           -> lenght of list
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._lenght = 0

    def add_first(self, item: Any) -> None:
        """Added fists element in list"""

        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._lenght += 1

    def add_last(self, item: Any) -> None:
        """Added last element in list"""
        if self._head is None:
            self.add_first(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._lenght += 1

    def remove_first(self) -> Any:
        """Remove first element from list"""
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._lenght -= 1
        return item

    def remove_last(self) -> Any:
        """Remove last element from list"""

        if self._head is self._tail:
            return self.remove_first()
        else:
            current = self._head
            while current.link is not self._tail:
                current = current.link
            item = self._tail.data
            self._tail = current
            self._tail.link = None
            self._lenght -= 1
            return item

    def __len__(self) -> int:
        """Return lenght of list"""

        return self._lenght
