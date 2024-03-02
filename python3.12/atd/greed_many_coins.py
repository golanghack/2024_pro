#! /usr/bin/env python3

from typing import List


def greed_many_coins(coin_values: List[int], change: int) -> None:
    """Greed algorithm for coins change
    
    >>> greed_many_coins([1, 5, 10, 25], 63)
    6
    >>> greed_many_coins([1, 21, 25], 63)
    15
    """

    coin_values.sort()
    coin_values.reverse()
    num_coins = 0
    for coin in coin_values:
        # add max coins is bigger
        num_coins += change // coin
        # update change
        change = change % coin
    return num_coins


if __name__ == "__main__":
    import doctest

    doctest.testmod()
