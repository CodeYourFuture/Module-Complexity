from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2) because we have two nested loops that iterate through the list of numbers.
    Space Complexity: O(1)
    Optimal time complexity: O(n)
    Explanation: The function checks every possible pair of numbers using two nested loops, resulting in O(n^2) time complexity.
    Refactor: It uses constant extra space. The optimal solution uses a set to check complements in O(1) time, reducing the overall complexity to O(n).
    """
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)

    return False
