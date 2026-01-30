from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n) - nested loops
    Space Complexity: O(n)
    Optimal time complexity: O(n)
    """
    seen_numbers = set()

    for num in numbers:
        match_num = target_sum - num

        if match_num in seen_numbers:
            return True
        seen_numbers.add(num)

    return False
