def has_pair_with_sum(numbers, target_sum):

    seen = set()

    for number in numbers:
        complement = target_sum - number

        if complement in seen:
            return True

        seen.add(number)

    return False


"""
Find if there is a pair of numbers that sum to a target value.

Time Complexity: O(n²)
Space Complexity: O(1)
Optimal Time Complexity: O(n)
"""