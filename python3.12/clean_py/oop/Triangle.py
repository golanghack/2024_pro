#! /usr/bin/env python3 

from typing import List

class Triangle:
    """Class Triangle is class the including operations for work with treangulum
    
    >>> tri = Triangle([1, 2, 3])
    >>> tri.sides()
    3
    >>> print(tri)
    'WOW Triangle"""
    
    def __init__(self, points: List[int]) -> None:
        self._sides = 3 # default sides for treangulum
        self._points = list(points)
        # detected a valid treangle
        if len(self._points) != 3:
            raise ValueError('Wrong number of points')
        
    def sides(self):
        return 3 
    
    def __str__(self) -> str:
        return 'WOW Triangle!'
    
    
        