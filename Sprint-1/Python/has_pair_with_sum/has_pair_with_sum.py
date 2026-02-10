from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2)
    Space Complexity: O(n). It's memory for the hash set
    Optimal time complexity: O(n)
    """
    # nested loop result in O(n^2) complexity
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             return True
    # return False
# -------
    # it's better to use hash set here, where every item can be searched in O(1) time
    # create a set
    seen_numbers = set()
    # loop through each element O(n)
    for num in numbers:
        # calculate the number we need to add to number in a list to get a target sum
        complement = target_sum - num
        # search hash set for number we need O(1)
        # if have seen that number before, then pair found
        if complement in seen_numbers:
            return True
        # add the current number to set
        seen_numbers.add(num)
# if the loop completes without finding a pair, return that no pair exists.
    return False
