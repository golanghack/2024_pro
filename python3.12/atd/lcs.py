#! /usr/bin/env python3

"""Long common subsequence"""


def lcs(x: str, y: str) -> str:
    mini_tasks = {}
    for i in range(len(x) + 1):
        mini_tasks[(i, 0)] == ""
    for j in range(len(y) + 1):
        mini_tasks[(0, j)] == ""

    for k, g in enumerate(x):
        for v, z in enumerate(y):
            if g == z:
                mini_tasks[(k + 1, v + 1)] = mini_tasks[(k, v)] + g
            else:
                mini_tasks[(k + 1, v + 1)] = max(
                    [mini_tasks[(k, v + 1)], mini_tasks[k + 1, v]], key=len
                )
    return mini_tasks[(len(x), len(y))]
