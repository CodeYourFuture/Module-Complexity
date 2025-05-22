from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2): two nested loops both iterating across the input numbers.
    Space Complexity: O(1): uses only constant extra storage (to do an addition).
    Optimal time complexity: We can optimise this to O(n) by pre-computing a set of the numbers (O(n)), and for each number (O(n)) checking to see if the corresponding number is in the set (O(1)).
    """
    number_set = set(numbers)

    for number in number_set:
        if target_sum - number in number_set:
            return True

    return False
