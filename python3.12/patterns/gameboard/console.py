#! /usr/bin/env python3

from consts import *


def console(char, background):
    return "\x1B[{}m{}\x1B[0m".format(43 if background == BLACK else 47, char or " ")
