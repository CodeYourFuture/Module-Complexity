from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    for i in range(len(numbers) - 1):

        if numbers[i] + numbers[i + 1] == target_sum:
            return True
            
    return False
