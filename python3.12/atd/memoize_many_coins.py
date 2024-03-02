#! /usr/bin/env python3

from typing import List, Dict


def memoize_many_coins(
    coins_values: List[int], change: int, known_results: Dict
) -> int:
    """ 
    >>> memoize_many_coins([1, 5, 10, 25], 63, {})
    6
    """
    min_coins = change
    if change in coins_values:
        known_results[change] = 1
        return 1
    elif change in known_results:
        return known_results[change]
    else:
        for i in [coin for coin in coins_values if coin <= change]:
            num_coins = 1 + memoize_many_coins(coins_values, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


if __name__ == "__main__":
    import doctest

    doctest.testmod()
