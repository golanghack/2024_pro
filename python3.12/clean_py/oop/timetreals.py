#! /usr/bin/env python3

import time
from typing import List, Callable


def timetrials(func: Callable, n: int, trials: int = 10) -> float:
    """Coverage timming work a function func"""

    total_time = 0
    for i in range(trials):
        start = time.time()
        func(list(range(n)))
        total_time += time.time() - start
    return total_time / trials, n


if __name__ == "__main__":
    n = 10000
    trials = 20
    result, steps = timetrials(sum, n, trials)
    print(f"average -> {result}  <--> {steps}")
