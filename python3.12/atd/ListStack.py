#! /usr/bin/env python3

from typing import Any


class ListStack:
    """Stack Data realisation with lists"""

    def __init__(self) -> None:
        self._list = []

    def push(self, item: Any) -> None:
        """Added new element in stack"""

        self._list.append(item)

    def pop(self) -> Any:
        """Remove element in stack and return"""

        return self._list.pop()

    def peek(self) -> Any:
        """Return last element from stack"""

        return self._list[-1]

    def isempty(self) -> bool:
        """Test empty stack"""

        return len(self._list) == 0

    def __len__(self) -> int:
        """Return length of stack"""

        return len(self._list)
