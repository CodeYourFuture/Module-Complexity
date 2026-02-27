from typing import List


cache = {}
coins = [200, 100, 50, 20, 10, 5, 2, 1]


def ways_to_make_change(total: int) -> int:

    cache.clear()
    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, coin_index: int) -> int:
    key = (total, coin_index)
    if key in cache:
        return cache[key]
    
    if total == 0:
        return 1
    if coin_index >= len(coins) or total < 0:
        return 0

    ways = 0
    coin = coins[coin_index]
    count_of_coin = 0
    
    while coin * count_of_coin <= total:
        ways += ways_to_make_change_helper(total - (coin * count_of_coin), coin_index + 1)
        count_of_coin += 1
    
    cache[key] = ways
    return ways
