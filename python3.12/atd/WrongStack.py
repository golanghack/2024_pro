#! /usr/bin/env python3

from typing import Any
from ListStack import ListStack


class WrongStack(ListStack):
    """Bad practic for building a stack"""

    def push(self, item: Any) -> None:
        """Added element in stack"""

        self._list.insert(0, item)

    def pop(self) -> Any:
        """Remove a first element from stack and return"""

        return self._list.pop(0)

    def peek(self) -> Any:
        """Return a first element from stack"""

        return self._list[0]
