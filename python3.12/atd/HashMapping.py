#! /usr/bin/env python3

from ListMapping import ListMapping
from EntryMapping import Entry


class HashMapping:
    def __init__(self, size=2):
        self._size = size
        self._buskets = [ListMapping() for i in range(self._size)]
        self._lenght = 0

    def put(self, key, value):
        mapp = self._busket(key)
        if key not in mapp:
            self._lenght += 1
        mapp[key] = value
        # test buskets
        if self._lenght > self._size:
            self._double()

    def get(self, key):
        mapp = self._busket(key)
        return mapp[key]

    def remove(self, key):
        mapp = self._busket(key)
        mapp.remove(key)

    def __contains__(self, key):
        mapp = self._busket(key)
        return key in mapp

    def _busket(self, key):
        return self._buskets[hash(key) % self._size]

    def _double(self):
        # old
        old_buskets = self._buskets
        # x2
        self._size *= 2
        # create new buskets
        self._buskets = [ListMapping() for i in range(self._size)]
        # added new elements
        for busk in old_buskets:
            for key, value in busk.items():
                # identification new
                mapp = self._busket(key)
                mapp[key] = value

    def __len__(self):
        return self._lenght

    def __iter__(self):
        for bus in self._buskets:
            for k in bus:
                yield k

    def values(self):
        for bus in self._buskets:
            for k, v in bus.items():
                yield k, v

    def __str__(self):
        item_list = [str(element) for bus in self._buskets for element in bus._entries]
        return "{" + ", ".join(item_list) + "}"

    __getitem__ = get
    __setitem__ = put
