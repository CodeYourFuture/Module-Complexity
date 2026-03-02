from typing import Dict, Tuple

COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def ways_to_make_change(total: int) -> int:
    """
    Returns the number of ways to make `total` using UK coin values.
    """
    cache: Dict[Tuple[int, int], int] = {}
    return _helper(total, 0, cache)


def _helper(total: int, coin_index: int, cache: Dict[Tuple[int, int], int]) -> int:
    """
    Recursive helper using memoization.

    Parameters:
    - total: remaining amount to form
    - coin_index: index into COINS representing which coins we are allowed to use
    - cache: memoization dictionary
    """

    # Base case: exact match
    if total == 0:
        return 1

    # Base case: no coins left
    if coin_index == len(COINS):
        return 0

    key = (total, coin_index)
    
    # If we’ve already solved: return the cached result, We just return the stored answer instead of recomputing it
    if key in cache:
        return cache[key]

    # CORE LOGIC: 
    ways = 0
    coin = COINS[coin_index]

    # Try using this coin 0, 1, 2, ... times
    # The maximum number of this coin we could use without exceeding total.
    max_count = total // coin

    # For each possible count of this coin, we compute the remaining amount and recursively call _helper for the next coin.
    for count in range(max_count + 1):
        remaining = total - (coin * count)
        ways += _helper(remaining, coin_index + 1, cache)

    cache[key] = ways
    return ways