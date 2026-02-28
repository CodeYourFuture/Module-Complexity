from typing import Dict, List, Tuple


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    cache: Dict[Tuple[int, int], int] = {}  # Initialize cache
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], cache, 0)


def ways_to_make_change_helper(total: int, coins: List[int], cache: Dict[Tuple[int, int], int], coin_index: int) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        return 1
    if total < 0 or coin_index >= len(coins):
        return 0
    
    
     # Check cache
    key = (total, coin_index)
    if key in cache:
        return cache[key]

    ways = 0
    coin = coins[coin_index]
    count_of_coin = 1
    while coin * count_of_coin <= total:
        remaining = total - coin * count_of_coin
        ways += ways_to_make_change_helper(remaining, coins, cache, coin_index + 1)
        count_of_coin += 1

    ways += ways_to_make_change_helper(total, coins, cache, coin_index + 1)    

    cache[key] = ways  # Store result in cache    
    return ways
