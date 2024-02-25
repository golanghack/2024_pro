#! /usr/bin/env python3


class Point:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def make(Cls, *args, **kwargs):
        return Cls(*args, **kwargs)
