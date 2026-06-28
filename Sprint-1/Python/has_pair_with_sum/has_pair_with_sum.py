from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: worst O(N^2) - square
    Space Complexity: O(numbers.length)
    Optimal time complexity: worth become O(N)
    """

    cheked_numbers = set()
    for number in numbers:
        complement = target_sum - number
        if complement in cheked_numbers:
            return True
        cheked_numbers.add(number)
    return False
