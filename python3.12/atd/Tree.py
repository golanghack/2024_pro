#! /usr/bin/env python3


class Tree:
    def __init__(self, _lists):
        iterator = iter(_lists)
        self.data = next(iterator)
        self.children = [Tree(elem) for elem in iterator]
