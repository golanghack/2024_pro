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
