from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Time Complexity: O(n)
    Space Complexity: O(1)
    Optimal Time Complexity: O(n)

    Refactor:
    The original implementation iterated through the list twice:
    once to calculate the sum and once to calculate the product.
    This refactor combines both calculations into a single loop,
    reducing the number of iterations while maintaining O(n)
    time complexity.

    Args:
        input_numbers: List of integers.

    Returns:
        Dictionary containing the sum and product.
    """

    total_sum = 0
    product = 1

    for number in input_numbers:
        total_sum += number
        product *= number

    return {
        "sum": total_sum,
        "product": product,
    }