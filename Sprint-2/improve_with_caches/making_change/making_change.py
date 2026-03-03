
from typing import List, Dict, Tuple

# Pre-create only 8 possible "coins" arrays
_BASE_COINS: List[int] = [200, 100, 50, 20, 10, 5, 2, 1]
COIN_SUFFIXES: List[Tuple[int, ...]] = [tuple(_BASE_COINS[i:]) for i in range(len(_BASE_COINS))]

cache: Dict[Tuple[int, int], int] = {}

def ways_to_make_change(total: int) -> int:
    cache.clear()
    # suffix_id == 0 identifies [200, 100, 50, 20, 10, 5, 2, 1]
    return ways_to_make_change_helper(total, suffix_id=0)


def ways_to_make_change_helper(total: int, suffix_id: int) -> int:
    """
    suffix_id uniquely identifies the subarray coins = COIN_SUFFIXES[suffix_id]
    where suffix_id in [0..7].
    """
    key = (total, suffix_id)
    if key in cache:
        return cache[key]

    coins = COIN_SUFFIXES[suffix_id]

    # Keep behavior close to original, but fix the standard base case:
    if total == 0:
        return 1
    if len(coins) == 0:
        return 0

    if len(coins) == 1:
        cache[key] = 1 if (total % coins[0] == 0) else 0
        return cache[key]

    ways = 0
    for coin_index in range(len(coins)):
        coin = coins[coin_index]
        count_of_coin = 1

        while coin * count_of_coin <= total:
            total_from_coins = coin * count_of_coin

            if total_from_coins == total:
                ways += 1
            else:
                # Instead of slicing coins[coin_index+1:], move the suffix_id forward.
                # suffix_id is the start index of `coins` in the base list, so:
                next_suffix_id = suffix_id + coin_index + 1
                if next_suffix_id < len(COIN_SUFFIXES):
                    ways += ways_to_make_change_helper(total - total_from_coins, suffix_id=next_suffix_id)

            count_of_coin += 1

    cache[key] = ways
    return ways
