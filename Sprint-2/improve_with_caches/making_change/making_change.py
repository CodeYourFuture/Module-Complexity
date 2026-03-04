
from typing import List, Dict, Tuple

# Pre-create only
_BASE_COINS: List[int] = [200, 100, 50, 20, 10, 5, 2, 1]

cache: Dict[Tuple[int, int], int] = {}

def ways_to_make_change(total: int) -> int:
    cache.clear()
    # suffix_id == 0 identifies [200, 100, 50, 20, 10, 5, 2, 1]
    return ways_to_make_change_helper(total, start_index: 0)


def ways_to_make_change_helper(total: int, start_index: int) -> int:
    if total == 0:
        return 1

    if start_index >= len(_BASE_COINS):
        return 0

    coin = _BASE_COINS[start_index]

    if start_index == len(_BASE_COINS) - 1:
        return 1 if total % coin == 0 else 0

    key = (total, start_index) 
    if key in cache:
        return cache[key]

    ways = 0

    for coin_index in range(start_index, len(_BASE_COINS)): 
        coin = _BASE_COINS[coin_index]
        count_of_coin = 1

        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin

            if total_from_coins == total:
                ways += 1
            else:
                ways += ways_to_make_change_helper(
                    total - total_from_coins,
                    coin_index + 1
                )

            count_of_coin += 1

    cache[key] = ways
    return ways
