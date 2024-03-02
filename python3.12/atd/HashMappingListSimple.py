#! /usr/bin/env python3

from ListMapping import ListMapping


class HashMappingListSimple:
    def __init__(self):
        self._size = 100
        self._buskets = [ListMapping() for i in range(self._size)]

    def put(self, key, value):
        mapp = self._busket(key)
        mapp[key] = value

    def _busket(self, key):
        return self._buskets[hash(key) % self._size]
