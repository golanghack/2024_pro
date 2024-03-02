#! /usr/bin/env python3


class Entry:
    """Implamentation Mapping dunctionality with list"""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " : " + str(self.value)
