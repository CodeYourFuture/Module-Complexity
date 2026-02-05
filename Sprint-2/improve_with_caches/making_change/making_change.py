def ways_to_make_change(total: int) -> int:
    cache = {}
    coins = (200, 100, 50, 20, 10, 5, 2, 1)

    def helper(remaining: int, start: int) -> int:
        if remaining == 0:
            return 1
        if remaining < 0 or start == len(coins):
            return 0

        key = (remaining, start)
        if key in cache:
            return cache[key]

        coin = coins[start]
        ways = 0

        max_count = remaining // coin
        for count in range(max_count + 1):
            ways += helper(remaining - count * coin, start + 1)

        cache[key] = ways
        return ways

    return helper(total, 0)
