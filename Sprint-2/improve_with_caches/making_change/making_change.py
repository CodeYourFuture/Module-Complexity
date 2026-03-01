from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    cache = {}
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], 0, cache)


def ways_to_make_change_helper(
    total: int, coins: List[int], coin_index: int, cache: dict
) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        return 1
    if coin_index == len(coins):
        return 0

    key = (total, coin_index)
    if key in cache:
        return cache[key]

    coin = coins[coin_index]
    ways = 0

    # the remaining coins can complete whatever total is left over
    while coin * count <= total:
        ways += ways_to_make_change_helper(total - coin * count, coins, coin_index + 1, cache)
        count += 1

    # counting combinations that don't use the current coin 
    ways += ways_to_make_change_helper(total, coins, coin_index + 1, cache)

    cache[key] = ways
    return ways
