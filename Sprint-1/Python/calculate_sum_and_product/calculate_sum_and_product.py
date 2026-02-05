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
    Time Complexity: O(n)
    The previous code iterated through the list twice (2n).
    I combined them into a single loop, so we iterate only once (n).

    Space Complexity: O(1) - We only use two variables (running_sum and running_product) regardless of the list size.
    Optimal time complexity: O(n) - We must visit every number at least once.
    """

    running_sum = 0
    running_product = 1

    # Refactor: Calculate both sum and product in one loop.
    for number in input_numbers:
        running_sum += number
        running_product *= number

    return {"sum": running_sum, "product": running_product}
