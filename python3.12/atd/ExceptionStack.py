#! /usr/bin/env python3

from typing import Any
from ListStack import ListStack


class ExceptionStack(ListStack):
    """Realisation stack with exceptions empty stack"""

    def pop(self) -> Any:
        """Remove an element from stack"""

        try:
            return self._list.pop()
        except IndexError:
            raise RuntimeError("pop from empty stack")
