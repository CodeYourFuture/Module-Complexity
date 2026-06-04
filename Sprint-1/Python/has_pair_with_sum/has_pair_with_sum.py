from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
        ANSWER: O(n)
        Because the list is looped through once.

    Space Complexity:
        ANSWER: O(n)
        Because a set is used to store seen numbers.

    Optimal time complexity:
        ANSWER: O(n)
        Each number is processed once using a set for faster lookup.

    Original Time Complexity: O(2n)

    """
    seen = set()

    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            return True
        seen.add(number)

    return False
