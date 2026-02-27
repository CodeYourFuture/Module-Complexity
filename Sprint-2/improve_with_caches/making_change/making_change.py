from typing import List


CACHE = {}
COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def ways_to_make_change(total: int) -> int:

    CACHE.clear()
    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, coin_index: int) -> int:
    if total == 0:
        return 1
    if coin_index >= len(COINS) or total < 0:
        return 0
    
    # Optimization: if this is the last coin, check if total is divisible by it
    if coin_index == len(COINS) - 1:
        return 1 if total % COINS[coin_index] == 0 else 0
    
    key = (total, coin_index)
    if key in CACHE:
        return CACHE[key]

    ways = 0
    coin = COINS[coin_index]
    count_of_coin = 0
    
    while coin * count_of_coin <= total:
        ways += ways_to_make_change_helper(total - (coin * count_of_coin), coin_index + 1)
        count_of_coin += 1
    
    CACHE[key] = ways
    return ways
