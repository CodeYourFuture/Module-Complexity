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
    for coin_index in range(len(coins)):
        count_of_coin = 1
        while coins * count_of_coin <= total:
            total_from_coins = coins * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                intermediate = ways_to_make_change_helper(total - total_from_coins, coins=coins[coin_index+1:])
                ways += intermediate
            count_of_coin += 1
            
    cache[key] = ways

    return ways
