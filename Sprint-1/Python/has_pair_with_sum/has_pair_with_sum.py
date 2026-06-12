from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: worst O(N!) - factorial
    Space Complexity: O(numbers.length)
    Optimal time complexity: worth become O(N)
    """

    for i in range(len(numbers)):
        if (numbers[i] - target_sum) in numbers:
            return True
    return False
