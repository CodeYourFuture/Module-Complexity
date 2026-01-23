from typing import List, Dict, Tuple

def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    memo: Dict[Tuple[int, int], int] = {}
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1], memo)


def ways_to_make_change_helper(total: int, coins: List[int], memo: Dict[Tuple[int, int], int]) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    Uses memoization to cache results for (total, coin_index).
    """
    if total == 0:
        return 1  
    if total < 0 or not coins:
        return 0  

    key = (total, len(coins))
    if key in memo:
        return memo[key]

    ways = 0
    coin_index = 0
    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            remainder = total - total_from_coins
            if remainder == 0:
                ways += 1
            else:
                intermediate = ways_to_make_change_helper(remainder, coins[coin_index + 1:], memo)
                ways += intermediate
            count_of_coin += 1

    memo[key] = ways
    return ways
