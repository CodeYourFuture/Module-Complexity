from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n)
    The previous code used nested loops (loop inside a loop), which is slow O(n^2).
    I used a Set to remember the numbers we have seen. This allows us to find the pair in one pass O(n).

    Space Complexity: O(n) - We store the visited numbers in a Set.
    Optimal time complexity: O(n) - We have to check each number at least once.
    """
    # Refactor: I used a Set to store numbers we have already seen.
    seen_numbers = set()

    for num in numbers:
        # Calculate the number we need to reach the target.
        match = target_sum - num

        # Check if the needed number is already in our set.
        if match in seen_numbers:
            return True

        # Add the current number to the set so we can use it later.
        seen_numbers.add(num)

    return False
