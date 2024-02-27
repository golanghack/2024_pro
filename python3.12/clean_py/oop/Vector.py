#! /usr/bin/env python3


class Vector:
    """Vector class implemtion vector of math
    
    >>> vector = Vector(1, 1)
    >>> vector.norm()
    1.4142135623730951
    """

    def __init__(self, x: float, y: float) -> None:
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            self.x = 0.0
            self.y = 0.0

    def norm(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __str__(self) -> str:
        return f"({self.x, self.y})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
