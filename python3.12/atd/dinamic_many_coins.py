#! /usr/bin/env python3

from typing import List, Dict


def dinamic_many_coins(coins_values: List[int], change) -> int:
    """
    >>> dinamic_many_coins([1, 5, 10, 21, 25], 63)
    3
    >>> dinamic_many_coins([1, 5, 10, 21, 25], 64)
    4
    """
    # create list for save results mini-tasks
    min_coins = [None] * (change + 1)
    # for every from 0 to sum shange find minimal
    for coin in range(change + 1):
        # try coints with as 1
        min_coins[coin] = coin
        # try conint solved with better when
        for c in coins_values:
            if coin >= c:
                min_coins[coin] = min(min_coins[coin], min_coins[coin - c] + 1)
    return min_coins[change]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
