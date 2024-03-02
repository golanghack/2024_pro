#! /usr/bin/env python3

from LinkedListListNode import LinkedListListNode


class DoubleLinkedListGood:
    def __init__(self):
        self._head = None
        self._tail = None
        self._lenght = 0

    def __len__(self):
        return self._lenght

    def _add_between(self, item, before, after):
        node = LinkedListListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._lenght += 1

    def add_first(self, item):
        self._add_between(item, None, self._head)

    def add_last(self, item):
        self._add_between(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._lenght -= 1
        return node.data

    def remove_first(self):
        return self._remove(self._head)

    def remove_last(self):
        return self._remove(self._tail)

    def __iadd__(self, other):
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                self._tail.link = other._head
                other._head.link = self._tail
            self._tail = other._tail
            self._lenght = self._lenght + other._lenght
            # clear other
            other.__init__()
        return self
