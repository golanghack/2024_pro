#! /usr/bin/env python3

from HashMapping import HashMapping


class BSTMapping(HashMapping):
    def __init__(self):
        self._root = None

    def get(self, key):
        if self._root:
            return self._root.get(key).value
        raise KeyError

    def put(self, key, value):
        if self._root:
            self._root = self._root.put(key, value)
        else:
            self._root = BSTNode(key, value)

    def __len__(self):
        return len(self._root) if self._root is not None else 0

    def _entry_iter(self):
        if self._root:
            yield from self._root

    def floor(self, key):
        if self._root:
            floor_node = self._root.floor(key)
            if floor_node is not None:
                return floor_node.key, floor_node.value
        return None, None

    def remove(self, key):
        if self._root:
            self._root = self._root.remove(key)
        else:
            raise KeyError

    def __delitem__(self, key):
        self.remove(key)
