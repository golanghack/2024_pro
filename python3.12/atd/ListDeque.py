#! /usr/bin/env python3

from typing import Any


class ListDequeue:
    """ 
    Realisation Deque data
    
    :add_first:         -> added element in start position in deque
    :add_last:          -> added element in end position in deque
    :remove_first:      -> remove first element from deque
    :remove_last:       -> remove last elemnt from deque
    :len:               -> lengh of deque
    
    """

    def __init__(self) -> None:
        self._list = []

    def add_first(self, item: Any) -> None:
        """Added firts element """

        self._list.insert(0, item)

    def add_last(self, item: Any) -> None:
        """Added last element"""

        self._list.append(item)

    def remove_first(self) -> Any:
        """Remove first element"""

        return self._list.pop(0)

    def remove_lat(self) -> Any:
        """Remove last element"""

        return self._list.pop()

    def __len__(self) -> int:
        """Return lenght a deque"""

        return len(self._list)
