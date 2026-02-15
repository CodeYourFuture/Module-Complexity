from typing import List, TypeVar

Number = TypeVar("Number", int, float)


"""
Find if there is a pair of numbers that sum to a target value.

Time Complexity:
    Before Refactor: O(n^2) — nested loops checking every pair.
    After Refactor:  O(n)   — O(1) set lookups.

Space Complexity:
    Before Refactor: O(1) — no additional data structure.
    After Refactor:  O(n) — in the worst case we store all numbers in numbers_seen.

Optimal Time Complexity:
    O(n) — achievable using a set to track previously seen numbers.
"""
def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
   numbers_seen = set()
   for current_num in numbers:  # O(n)
        required_num = target_sum - current_num
        if required_num in numbers_seen:
            return True
        numbers_seen.add(current_num)
   return False
