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
    Time Complexity:
      There were two separated loops, one for each operation. Each had complexity O(n)
      The refactor combined them into a single loop reducing the constant factor, maintaining the same Big-O complexity.
    Space Complexity:
        space is constant O(1)
    Optimal time complexity:
        With one loop for both operations, must iterate through all n elements in the list, so the overall time complexity is O(n).
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    product = 1
    for current_number in input_numbers:
        sum += current_number
        product *= current_number

    return {"sum": sum, "product": product}
