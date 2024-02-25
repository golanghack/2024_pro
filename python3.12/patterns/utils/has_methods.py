#! /usr/bin/env python3 

from typing import List

def has_methods(*methods: List[str]):
    def decorator(Base):
        def __subclasshook__(Class, Subclass):
            if Class is Base:
                needed = set(methods)
                for Superclass in Subclass.__mro__:
                    for meth in needed.copy():
                        if meth in Superclass.__dict__:
                            needed.discard(meth)
                    if not needed:
                        return True
            return NotImplemented
        Base.__subclasshook__ = classmethod(__subclasshook__)
        return Base 
    return decorator

