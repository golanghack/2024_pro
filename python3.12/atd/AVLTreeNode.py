#! /usr/bin/env python3

from BalancedBSTMapping import BalancedBSTNode


def height(node):
    return node.height if node else -1


def update(node):
    if node:
        node._update_left()
        node._update_right()


class AVLTreeNode(BalancedBSTNode):
    def __init__(self, key, value):
        BalancedBSTNode.__init__(self, key, value)
        self._update_lenght()

    def new_node(self, key, value):
        return AVLTreeNode(key, value)

    def _update_height(self):
        self.height = 1 + max(height(self.left, height(self.right)))

    def balance(self):
        return height(self.right) - height(self.left)

    def rebalance(self):
        bal = self.balance()
        if bal == -2:
            if self.left.balance() > 0:
                self.left = self.left.rotate_left()
            new_root = self.rotate_right()
        elif bal == 2:
            if self.right.balance() < 0:
                self.right = self.right.rotate_right()
            new_root = self.rotate_left()
        else:
            return self
        update(new_root.left)
        update(new_root.right)
        update(new_root)
        return new_root

    def put(self, key, value):
        new_root = BalancedBSTNode.put(self, key, value)
        update(new_root)
        return new_root.rebalance()

    def remove(self, key):
        new_root = BalancedBSTNode.remove(self, key)
        update(new_root)
        return new_root.rebalance() if new_root else None
