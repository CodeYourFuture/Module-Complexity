from typing import List, Tuple, Dict


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, [200, 100, 50, 20, 10, 5, 2, 1])


def ways_to_make_change_helper(total: int, coins: List[int], memo: Dict[Tuple[int, int], int] = None) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    Uses memoization to optimize repeated subproblems.
    """
    if memo is None:
        memo = {}
    key = (total, len(coins))
    if key in memo:
        return memo[key]
    if total == 0:
        return 1
    if total < 0 or len(coins) == 0:
        return 0
    ways = 0
    coin = coins[0]
    for count_of_coin in range(0, total // coin + 1):
        remaining = total - coin * count_of_coin
        ways += ways_to_make_change_helper(remaining, coins[1:], memo)
    memo[key] = ways
    return ways
