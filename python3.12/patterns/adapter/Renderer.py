#! /usr/bin/env python3

import abc
from has_methods import has_methods


@has_methods("header", "paragraph", "footer")
class Renderer(abc.ABCMeta):
    pass
