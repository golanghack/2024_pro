#! /usr/bin/env python3


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
