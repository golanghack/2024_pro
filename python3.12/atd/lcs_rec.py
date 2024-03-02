#! /usr/bin/env python3

"""Longest common subsequence"""


def lcs_rec(x: str, y: str) -> str:
    if x == "" or y == "":
        return ""
    if x[-1] == y[-1]:
        return lcs_rec(x[:-1], y[:-1]) + x[-1]
    else:
        return max([lcs_rec(x[:-1], y), lcs_rec(x, y[:-1])], key=len)
