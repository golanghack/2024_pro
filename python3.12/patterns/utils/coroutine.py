#! /usr/bin/env python3

import functools
from typing import Callable


def coroutine(function: Callable) -> Callable:
    """Create coroutine decorator"""

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator

    return wrapper
