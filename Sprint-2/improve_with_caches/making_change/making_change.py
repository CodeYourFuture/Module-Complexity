def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    cache = {}
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    return ways_to_make_change_helper(total, coins, 0, cache)


def ways_to_make_change_helper(total: int, coins: tuple, coin_index: int, cache: dict) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0 or coin_index >= len(coins):
        return 0

    cache_key = (total, coin_index)
    
    if cache_key in cache:
        return cache[cache_key]

    ways = 0
    for i in range(coin_index, len(coins)):
        coin = coins[i]
        count_of_coin = 1
        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin
            if total_from_coins == total:
                ways += 1
            else:
                intermediate = ways_to_make_change_helper(total - total_from_coins, coins, i + 1, cache)
                ways += intermediate
            count_of_coin += 1
    
    cache[cache_key] = ways
    return ways
