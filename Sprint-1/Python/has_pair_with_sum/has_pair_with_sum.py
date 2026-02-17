from typing import List, TypeVar, Set

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.
    This uses a hash set (Python's set) to achieve O(N) time complexity.

    Time Complexity: O(N)
    Space Complexity: O(N)
    Optimal time complexity: O(N)
    """
    seen_numbers: Set[Number] = set()

    # Iterate through the list once (O(N) time)
    for current_num in numbers:
        complement = target_sum - current_num

        # Check if the required complement is already in the set (O(1) average time)
        if complement in seen_numbers:
            return True

        # Add the current number to the set for future lookups
        seen_numbers.add(current_num)

    return False

'''
The complexity is driven by the nested for loops
The bottleneck is the inner loop, which forces us to check every possible pair. 
We can use a Hash Set (a set in Python) to store the numbers we've already seen. 
This allows us to perform lookups in O(1) average time.

Complexity of Refactor
Time Complexity: O(N)(Linear Time). 
The function performs a single pass over the N elements, with constant-time operations inside the loop. 
This is the optimal complexity.

Space Complexity: 
O(N)(Linear Space). We introduce the seen_numbers set, which, in the worst case, 
will store up to N elements from the input list.

Resources: https://www.w3schools.com/python/ref_set_intersection.asp

'''