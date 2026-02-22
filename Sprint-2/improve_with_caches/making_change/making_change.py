from typing import List
cache = {}

def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    coins = [200, 100, 50, 20, 10, 5, 2, 1] 
    return ways_to_make_change_helper(total, coins, 0)


def ways_to_make_change_helper(total: int, coins: List[int],start_index: int) -> int:
 
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
#We found one valid way if its an exact match.
    if total == 0:
        return 1
# No coins left to try as we moved past the end of the list
    if start_index >= len(coins): 
        return 0

# Cache key now uses (total, start_index) instead of hashing the whole coin list
    key = (total, start_index)
    if key in cache:
        return cache[key]

    ways = 0

 # Try using the current coin 1,2,3... times as long as we don't exceed the total.
    coin = coins[start_index]
    count_of_coin = 1

    while coin * count_of_coin <= total:
        total_from_coins = coin * count_of_coin

        if total_from_coins == total:
# if exact match then one valid way

            ways += 1
        else:
# Remaining total, and move to the next coin (no slicing!)
            intermediate = ways_to_make_change_helper(
                total - total_from_coins,
                coins,
                start_index + 1
            )
            ways += intermediate

        count_of_coin += 1

# Also consider the case where we skip this coin entirely
    ways += ways_to_make_change_helper(total, coins, start_index + 1)

    cache[key] = ways
    return ways
