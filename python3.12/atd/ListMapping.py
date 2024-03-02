#! /usr/bin/env python3

from EntryMapping import Entry


class ListMapping:
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        element = self._entry(key)
        if element is not None:
            element.value = value
        else:
            self._entries.append(Entry(key, value))

    def get(self, key):
        element = self._entry(key)
        if element is not None:
            return element.value
        else:
            raise KeyError

    def remove(self, key):
        element = self._entry(key)
        if element is not None:
            self._entries.remove(element)

    def _entry(self, key):
        for element in self._entries:
            if element.key == key:
                return element
        return None

    def __str__(self):
        return "{" + ", ".join(str(elem) for elem in self._entries) + "}"

    def __len__(self):
        return len(self._entries)

    def __contains__(self, key):
        if self._entry(key) is None:
            return False
        else:
            return True

    def __iter__(self):
        return (elem.key for elem in self._entries)

    def values(self):
        return (elem.value for elem in self._entries)

    def items(self):
        return ((elem.key, elem.value) for elem in self._entries)

    __getitem__ = get
    __setitem__ = put
