#! /usr/bin/env python3

from EntryMapping import Entry


class ListMappingSimple:
    """Create map atd with lists"""

    def __init__(self) -> None:
        self._entries = []

    def put(self, key, value):
        for element in self._entries:
            if element.key == key:
                element.value = value
                return
        self._entries.append(Entry(key, value))

    def get(self, key):
        for element in self._entries:
            if element.key == key:
                return element.value
        raise KeyError
