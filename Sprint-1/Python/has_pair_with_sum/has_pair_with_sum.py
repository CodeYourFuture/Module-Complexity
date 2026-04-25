from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n²) - where n is the length of the input array. We use two nested loops, where the outer loop
                     iterates through each element, and the inner loop iterates through all subsequent elements.
                     In the worst case, we need to check all pairs.
    Space Complexity: O(1) - We only use constant extra space for loop variables.
    Optimal time complexity: O(n) - Using a hash set allows us to check if the complement (target_sum - current_number)
                             exists in O(1) time, reducing the overall complexity from O(n²) to O(n) with one pass through the array.
    """
    # Optimised approach: Use a set to store seen numbers for O(1) lookups
    seen_numbers = set()

    for num in numbers:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)

    return False
