from typing import List
cache = {}
COINS = [200, 100, 50, 20, 10, 5, 2, 1]
COINT_TYPES_NUM = len(COINS)

def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, coin_index: int) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if (total, coin_index) in cache:
        return cache[(total, coin_index)]

    if total == 0:
        return 1

    if coin_index == COINT_TYPES_NUM:
        return 0


    ways = 0
    coin = COINS[coin_index]
    count_of_coin = 0
    while count_of_coin * coin <= total:
        ways += ways_to_make_change_helper(
            total - count_of_coin * coin,
            coin_index + 1
        )
        count_of_coin += 1
    
    cache[(total, coin_index)] = ways
    return ways
