# cache dictionary, key is (total, tuple_of_coins)
_change_cache = {}

def ways_to_make_change(total: int) -> int:
    """
    Given access to coins with the values 1, 2, 5, 10, 20, 50, 100, 200, returns a count of all of the ways to make the passed total value.

    For instance, there are two ways to make a value of 3: with 3x 1 coins, or with 1x 1 coin and 1x 2 coin.
    """
    _change_cache.clear()
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    return ways_to_make_change_helper(total, tuple(coins))


def ways_to_make_change_helper(total: int, coins: tuple) -> int:
    """
    Helper function for ways_to_make_change to avoid exposing the coins parameter to callers.
    """
    if total == 0:
        return 1
    if not coins:
        return 0

    key = (total, coins)
    if key in _change_cache:
        return _change_cache[key]
    
    coin = coins[0]
    rest = coins[1:]

    ways = 0
    count_of_coin = 0
 
    while coin * count_of_coin <= total:
        total_from_coins = coin * count_of_coin
        intermediate = ways_to_make_change_helper(total - total_from_coins, rest)
        ways += intermediate
        count_of_coin += 1
    
    _change_cache[key] = ways
    return ways
