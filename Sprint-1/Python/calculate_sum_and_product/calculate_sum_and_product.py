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
        ANSWER: O(n)
        Because the list is looped through once.

    Space Complexity:
        ANSWER: O(1)
        Because only two variables are used.

    Optimal time complexity:
        ANSWER: O(n)
        Each number is processed once.

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
