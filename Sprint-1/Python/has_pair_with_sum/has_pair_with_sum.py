from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2)
    Space Complexity: O(n). It's memory for the input array arr
    Optimal time complexity: O(n)
    """
    # nested loop result in O(n^2) complexity
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             return True
    # return False

    # it's better to use to pointers method here
    # first: sort the list O(n)
    numbers = sorted(numbers)
    # declare the left and right pointers
    left, right = 0, len(numbers)-1
    # and until we "squeezed" the list check if sum of the pointers is equal to target sum
    # in worst case we need to do n-1 steps where n is length of the list, so overall complexity will be O(n)
    while left < right:
        currentSum = numbers[left]+numbers[right]
        if currentSum == target_sum:
            return True
        if currentSum > target_sum:
            right -= 1
        else:
            left+=1
    return False