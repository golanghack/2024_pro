#! /usr/bin/env python3

from typing import List


def rec_many_coins(coins_values: List[int], change: int):
    """ 
    >>> rec_many_coins([1, 21, 25], 63)
    3
    >>> rec_many_coins([1, 5, 21, 25], 63)
    3
    """
    min_coins = change
    if change in coins_values:
        return 1
    else:
        for i in [coin for coin in coins_values if coin <= change]:
            num_coins = 1 + rec_many_coins(coins_values, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


if __name__ == "__main__":
    import doctest

    doctest.testmod()
