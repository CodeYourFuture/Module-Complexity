from typing import List, Tuple, Dict

change_cache: Dict[Tuple[int, int], int] = {}
def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1],0)


def ways_to_make_change_helper(total: int, coins: List[int], coin_index: int) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    
    # If total is 0, we found 1 valid way
    if total == 0:
        return 1
        
    # If total becomes negative or we ran out of coins, 0 ways
    if total < 0 or coin_index >= len(coins):
        return 0

    # shortcut if only one coin is left
    if coin_index == len(coins) - 1:
        return 1 if total % coins[coin_index] == 0 else 0

    # Cache check
    cache_key = (total, coin_index)
    if cache_key in change_cache:
        return change_cache[cache_key]

    ways = 0
    current_coin = coins[coin_index]
    
    # One level of loop to try taking 0, 1, 2... of the current coin
    current_total = 0
    while current_total <= total:
        ways += ways_to_make_change_helper(total - current_total, coins, coin_index + 1)
        current_total += current_coin

    # Store the result in the cache before returning      
    change_cache[cache_key] = ways
    return ways
