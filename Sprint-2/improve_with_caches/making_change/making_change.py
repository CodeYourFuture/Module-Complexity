from typing import List

coins = [200, 100, 50, 20, 10, 5, 2, 1]

cache = {}

def ways_to_make_change(total: int) -> int:

    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, coin_index :int) -> int:
    key = (total, coin_index)
    

    if coin_index == len(coins):
        return 0

    ways = 0
   
    coin = coins[coin_index]
    count_of_coin = 0
    while count_of_coin * count_of_coin <= total:
        ways += ways_to_make_change_helper(
            total - count_of_coin * coin,
            coin_index + 1
        )
        count_of_coin += 1
            
    cache[key] = ways

    return ways
