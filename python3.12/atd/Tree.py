#! /usr/bin/env python3


class Tree:
    def __init__(self, _lists):
        iterator = iter(_lists)
        self.data = next(iterator)
        self.children = [Tree(elem) for elem in iterator]

    def __str__(self, level=0):
        tree_string = " " * level + str(self.data)
        for child in self.children:
            tree_string += "\n" + child.__str__(level + 1)
        return tree_string
