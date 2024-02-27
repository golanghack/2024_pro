#! /usr/bin/env python3

from typing import Any


class LimitList:
    """Limited list lenght"""

    def __init__(self) -> None:
        self._l = []

    def append(self, item: Any) -> None:
        self._l.append(item)

    def __getitem__(self, index: int):
        return self._l[index]
