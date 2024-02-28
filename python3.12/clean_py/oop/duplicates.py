#! /usr/bin/env python3

from typing import List


def duplicates(into_list: List):
    s = set()
    return any(element in s or s.add(element) for element in into_list)


if __name__ == "__main__":
    into_list = [12, 12, 4, 5, 3]
    dups = duplicates(into_list)
    print(dups)
