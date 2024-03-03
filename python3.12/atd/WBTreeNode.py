#! /usr/bin/env python3

from BalancedBST import BalancedBST
from BalancedBSTMapping import BalancedBSTNode


class WBTreeNode(BalancedBSTNode):
    def new_node(self, key, value):
        return WBTreeNode(key, value)

    def too_light(self, other):
        other_lenght = len(other) if other else 0
        return len(self) + 1 >= 4 * (other_lenght + 1)

    def rebalance(self):
        if self.too_light(self.left):
            if self.too_light(self.right.right):
                self.right = self.right.rotateright()
            new_root = self.rotate_left()
        elif self.too_light(self.right):
            if self.too_light(self.left.left):
                self.left = self.left.rotate_left()
            new_root = self.rotate_right()
        else:
            return self
        return new_root

    def put(self, key, value):
        new_root = BalancedBSTNode.put(self, key, value)
        return new_root.rebalance()

    def remove(self, key):
        new_root = BalancedBSTNode.remove(self, key)
        return new_root.rebalance() if new_root else None
