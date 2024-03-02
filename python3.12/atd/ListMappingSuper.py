#! /usr/bin/env python3

from SuperMapping import Mapping
from EntryMapping import Entry


class ListMappingSuper:
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

    def _entry(self, key):
        for element in self._entries:
            if element.key == key:
                return element
        return None

    def _entry_iter(self):
        return iter(self._entries)

    def __len__(self):
        return len(self._entries)
