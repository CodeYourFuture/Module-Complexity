from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    seen_numbers = set()

    for current_number in numbers:
        needed_partner = target_sum - current_number

        if needed_partner in seen_numbers:
            return True

        seen_numbers.add(current_number)

    return False

#because old code have a nested loop (a loop inside a loop), itsmatching every number against every other single number in the list
"""
    new function go through the list just once, for each number, 
    it finds the exact "matching partner" needed to reach the target. 
    It saves everything it sees into a Set so it can check for that partner 
 completely avoiding slow nested loops.
    """

"""
Time Complexity (Original): O(N^2) — The original code used a loop inside a loop (i and j). Because it had to manually check every possible combination of numbers, it became incredibly slow when dealing with large lists.
Space Complexity (Improved): O(N) — The improved version uses extra memory to store the numbers inside the seen_numbers set as it loops through them.
Optimal Time Complexity (Improved): O(N) — By using a set, checking if needed_partner in seen_numbers is instant. The code now only needs to look at each number in the list exactly one time, making it lightning-fast.
"""
