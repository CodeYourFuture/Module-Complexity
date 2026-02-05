from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Areas of inefficiency in original version:
    - Nested loops check all possible pairs, leading to quadratic time

    Time Complexity: O(n) average
    Space Complexity: O(n)
    Optimal time complexity: O(n)

    - set to track previously seen values.
    """
    seen = set()

    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            return True
        seen.add(number)

    return False
