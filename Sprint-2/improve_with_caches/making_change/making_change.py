from typing import List

cache = {}
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, 0)
    


def ways_to_make_change_helper(total: int, index: int) -> int:
    key = (total, index)
    if key in cache:
        return cache[key]
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        cache[key] = 1
        return 1
    
    if index == len(coins):
        cache[key] = 0
        return 0

    coin=coins[index]
    ways = 0
    count = 0
    while coin * count <= total:
        ways += ways_to_make_change_helper(total - coin * count, index + 1)
        count +=1
    cache[key] = ways
    return ways