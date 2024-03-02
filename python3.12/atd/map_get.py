#! /usr/bin/env python3


def map_get(_list, key):
    for element in _list:
        if element.key == key:
            return element.value
    raise KeyError
