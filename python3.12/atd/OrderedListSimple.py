#! /usr/bin/env python3


class OrderedListSimple:
    def __init__(self):
        self._list = []

    def add(self, item):
        self._list.append(item)
        self._list.sort()

    def remove(self, item):
        self._list.remove(item)

    def __getitem__(self, index):
        return self._list[index]

    def __contains__(self, item):
        return item in self._list

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        return iter(self._list)
