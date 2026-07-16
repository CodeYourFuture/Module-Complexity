from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2) - nested loops compare every pair
    Space Complexity: O(1) - no extra data structures
    Optimal time complexity: O(n) - using a set to store seen numbers
    """
    seen = set()

    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)

    return False
