#! /usr/bin/env python3

from queue import Queue


class Tree:
    def __init__(self, _lists):
        iterator = iter(_lists)
        self.data = next(iterator)
        self.children = [Tree(elem) for elem in iterator]

    def _list_with_levels(self, level, trees):
        trees.append(" " * level + str(self.data))
        for child in self.children:
            child._list_with_levels(level + 1, trees)

    def __str__(self):
        trees = []
        self._list_with_levels(0, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def height(self):
        if len(self.children) == 0:
            return 0
        return 1 + max(child.height() for child in self.children)

    def __contains__(self, key):
        return self.data == key or any(key in ch for ch in self.children)

    def preorder(self):
        yield self.data
        for child in self.children:
            for data in child.preorder():
                yield data

    __iter__ = preorder

    def _postorder(self):
        node, child_iter = self, iter(self.children)
        stack = [(node, child_iter)]
        while stack:
            node, child_iter = stack[-1]
            try:
                child = next(child_iter)
                stack.append(child, iter(child.children))
            except StopIteration:
                yield node
                stack.pop()

    def postorder(self):
        return (node.data for node in self._postorder())

    def _layer_order(self):
        node, child_iter = self, iter(self.children)
        queue = Queue()
        queue.enqueue((node, child_iter))
        while queue:
            node, child_iter = queue.peek()
            try:
                child = next(child_iter)
                queue.enqueue((child, iter(child.children)))
            except StopIteration:
                yield node

    def layer_order(self):
        return (node.data for node in self._layer_order())
