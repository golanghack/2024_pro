#! /usr/bin/env python3


from typing import List


class Polygon:
    def __init__(self, sides: int, points: List[int]) -> None:
        self._sides = sides
        self._points = list(points)
        if len(self._points) != self._sides:
            raise ValueError("Wrong number of points")

    def sides(self):
        return self._sides


# USED


class Square(Polygon):
    def __init__(self, points: List[int]) -> None:
        Polygon.__init__(self, 4, points)

    def __str__(self) -> str:
        return "Square"
