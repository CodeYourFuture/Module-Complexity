from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:    O(n^2) because it loops twice to check for the possible pairs.
    Space Complexity:   O(1) because no extra space is used in the process.
    Optimal time complexity:    O(n) can be possible if sets are used.
    """
    # for i in range(len(numbers) - 1):

    #     for j in range(i + 1, numbers):
    #         if numbers[i] + numbers[i + 1] == target_sum:
    #             return True
            
    # return False

    seen = set()

    for num in numbers:
        if target_sum - num in seen:
            return True
        seen.add(num)
    return False
