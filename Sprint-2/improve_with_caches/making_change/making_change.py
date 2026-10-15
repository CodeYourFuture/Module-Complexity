COINS = (200, 100, 50, 20, 10, 5, 2, 1)
cache = {}

def ways_to_make_change(total: int) -> int:
    return ways_to_make_change_helper(total, 0)


def ways_to_make_change_helper(total: int, coin_index: int) -> int:
    if total == 0:
        return 1

    if total < 0 or coin_index == len(COINS):
        return 0

    key = (total, coin_index)

    if key in cache:
        return cache[key]

    coin = COINS[coin_index]

    ways = 0

    for count in range(total // coin + 1):
        remaining = total - count * coin

        ways += ways_to_make_change_helper(remaining, coin_index + 1)

    cache[key] = ways

    return ways
