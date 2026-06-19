from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], coin_index = 0, cache = None)


def ways_to_make_change_helper(total: int, coins: List[int], coin_index: int = 0, cache: dict = None) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if cache == None:
        cache = {}

    current_key = (total, coin_index)
    if current_key in cache:
        return cache[current_key]
    
    if total == 0:
        return 1

    if total < 0 or coin_index >= len(coins):
        return 0

    ways = 0
    
    remaining_value = total - coins[coin_index]
    
    taken_the_coin = ways_to_make_change_helper(remaining_value, coins, coin_index, cache)

    left_the_coin = ways_to_make_change_helper(total, coins, coin_index + 1, cache)

    ways = taken_the_coin + left_the_coin

    cache[current_key] = ways
    return ways
