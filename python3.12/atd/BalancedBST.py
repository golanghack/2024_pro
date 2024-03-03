#! /usr/bin/env python3

from BSTMapping import BSTMapping
from BalancedBSTMapping import BalancedBSTNode


class BalancedBST(BSTMapping):
    Node = BalancedBSTNode

    def put(self, key, value):
        if self._root:
            self._root = self._root.put(key, value)
        else:
            self._root = self.Node(key, value)
