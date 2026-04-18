from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    memo = {}
    return ways_to_make_change_helper(total, coins, 0, memo)

def ways_to_make_change_helper(total: int, coins: List[int], coin_index: int, memo: dict) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        return 1

    if coin_index == len(coins):
        return 0
    
    key = (total, coin_index)

    if key in memo:
        return memo[key]


    ways = 0
    coin = coins[coin_index]
    count_of_coin = 0

    while count_of_coin * coin <= total:
        remaining = total - count_of_coin * coin
        ways += ways_to_make_change_helper(remaining, coins, coin_index + 1, memo)
        count_of_coin += 1
    
    memo[key] = ways

    return ways
