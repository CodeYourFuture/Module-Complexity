from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    Time Complexity: O(n) - two loops over all of the input numbers, each of which is O(n).
    Space Complexity:  O(1) - uses two numbers of additional space, regardless of input size.
    Optimal time complexity: The current implementation is asymptotically optimal - we fundamentally do need to look at every number in order to sum/product them. We could combine the two loops into two to avoid the overhead of tracking a second iteration, but this wouldn't change the complexity.
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    for current_number in input_numbers:
        sum += current_number

    product = 1
    for current_number in input_numbers:
        product *= current_number

    return {"sum": sum, "product": product}
