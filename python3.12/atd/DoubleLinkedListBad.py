#! /usr/bin/env python3

from LinkedListListNode import LinkedListListNode


class DoubleLinkedList:
    """Double Linked List atd"""

    def __init__(self):
        self._head = None
        self._tail = None
        self._lenght = 0

    def add_first(self, item):
        if len(self) == 0:
            self._head = self._tail = LinkedListListNode(item, None, None)
        else:
            new_node = LinkedListListNode(item, None, self._head)
            self._head.prev = new_node
            self._head = new_node
            self._lenght += 1

    def add_last(self, item):
        if len(self) == 0:
            self._head = self._tail = LinkedListListNode(item, None, None)
        else:
            new_node = LinkedListListNode(item, self._tail, None)
            self._tail.link = new_node
            self._tail = new_node
        self._lenght += 1

    def __len__(self):
        return self._lenght
