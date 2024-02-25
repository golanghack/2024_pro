#! /usr/bin/env python3

import abc
import collections


class Requirer(abc.ABCMeta):
    @classmethod
    def __subclasshook__(Class, Subclass) -> bool:
        methods = set()
        for Superclass in Subclass.__mro__:
            if hasattr(Superclass, "required_methods"):
                methods |= set(Superclass.required_methods)
        attributes = collections.ChainMap(
            *(Superclass.__dict__ for Superclass in Class.__mro__)
        )
        if all(method in attributes for method in methods):
            return True
        return NotImplemented
