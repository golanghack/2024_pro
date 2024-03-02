#! /usr/bin/env python3

from EntryMapping import Entry


def map_put(_list, key, value):
    for element in _list:
        if element.key == key:
            element.value = value
            return
    _list.append(Entry(key, value))
