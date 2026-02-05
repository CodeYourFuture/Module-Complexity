from typing import List
def ways_to_make_change(total: int) -> int:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    cache = {}  # To store already calculated results

    def count_ways(remaining, index):
        # Base cases
        if remaining == 0:
            return 1  # Found a valid combination
        if remaining < 0 or index == len(coins):
            return 0  # Not possible
        # Check cache
        key = (remaining, index)
        if key in cache:
            return cache[key]
        # Option 1: use current coin (stay on same index)
        use_it = count_ways(remaining - coins[index], index)
        # Option 2: skip current coin (move to next index)
        skip_it = count_ways(remaining, index + 1)
        # Store result in cache
        cache[key] = use_it + skip_it
        return cache[key]
    return count_ways(total, 0)



#Time Complexity O(total × number of coins)
# Space Complexity O(total × number of coins)
#less expensive in relation to the original function
