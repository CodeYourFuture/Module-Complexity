from typing import List

def ways_to_make_change(total: int) -> int:
    cache = {}
    return ways_to_make_change_helper(total, (200, 100, 50, 20, 10, 5, 2, 1), cache)

def ways_to_make_change_helper(total: int, coins: tuple, cache: dict) -> int:
    if total == 0 or len(coins) == 0:
        return 0
    cache_key = (total, coins)
    if cache_key in cache:
        return cache[cache_key]
    ways = 0
    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                intermediate = ways_to_make_change_helper(
                    total - total_from_coins,
                    coins=coins[coin_index + 1:],
                    cache=cache
                )
                ways += intermediate
            count_of_coin += 1
    cache[cache_key] = ways
    return ways