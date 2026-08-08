from typing import List, Tuple, Dict


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    cache: Dict[Tuple[int, int], int] = {}
    return ways_to_make_change_helper(total, coins, 0, cache)


def ways_to_make_change_helper(
    total: int, coins: List[int], coin_index: int, cache: Dict[Tuple[int, int], int]
) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        return 1
    if total < 0 or coin_index == len(coins):
        return 0

    key = (total, coin_index)
    if key in cache:
        return cache[key]

    coin = coins[coin_index]
    ways = 0
    count = 0
    while count * coin <= total:
        remaining = total - count * coin
        ways += ways_to_make_change_helper(remaining, coins, coin_index + 1, cache)
        count += 1

    cache[key] = ways
    return ways
