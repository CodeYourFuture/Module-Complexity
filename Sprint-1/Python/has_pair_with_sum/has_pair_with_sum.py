from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(N^2), a loop inside a loop
    Space Complexity: O(1). O(1) is for the i and j loop counter.
    Optimal time complexity: O(N) as it only loops once, with a trade off space becomes O(N).
    """
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             return True
    # return False

    pair_num_set = set()

    for num in numbers:
        pair_num = target_sum - num
        if pair_num in pair_num_set:
            return True
        else:
            pair_num_set.add(num)
    return False
