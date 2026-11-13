from typing import List, Dict, Tuple


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """

    # pass in a cache to the helper function
    # the cache key is a total and the start of the sublist for a given call to the helper function
    cache: Dict[Tuple[int, int], int] = {}

    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], 0, cache)


def ways_to_make_change_helper(
    total: int, 
    coins: List[int], 
    start: int, 
    cache: Dict[Tuple[int, int], int]
    ) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.

    Tries to make the least amount of changes to existing code, and rely on caching to improve performance.

    Checks cache for a given key (remaining amount, remaining coins)
    if not in cache, then cacluate the the ways for that remaining amount and remaining keys, same as before,
    add that to the cache, so that subsequence calls to helper function with same parameters is not recalculated.
    """
    if total == 0 or len(coins) == 0:
        return 0

    # if only one coin left, don't do recursive step
    if start == len(coins) - 1:
        return 1 if total % coins[start] == 0 else 0

    key = (total, start)
    if key in cache:
        return cache[key]


    ways = 0
    for coin_index in range(start, len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(total - total_from_coins, coins, coin_index + 1, cache)
            count_of_coin += 1
    cache[key] = ways
    return ways