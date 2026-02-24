from typing import List


def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """

    coins=[200, 100, 50, 20, 10, 5, 2, 1]
    all_subarrays=[]
    for i  in range(len(coins)) :
        all_subarrays.append( coins[i:] )

    cache={}    
         
    return ways_to_make_change_helper(total, all_subarrays,0,cache)


def ways_to_make_change_helper(total: int, all_subarrays: List[List[int]],subarray_id: int,cache) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0 or subarray_id >= len(all_subarrays) :
        return 0
    
    key = (total, subarray_id)
    if key in cache:
        return cache[key]
    
    coins = all_subarrays[subarray_id]    
    ways = 0
    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(total - total_from_coins, all_subarrays, subarray_id + coin_index + 1, cache)
               
            count_of_coin += 1

    cache[key]=ways   

    return ways
