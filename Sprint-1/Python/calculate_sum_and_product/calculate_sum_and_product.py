from typing import Dict, List

def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:

    total_sum = 0
    total_product = 1

    for number in input_numbers:
        total_sum += number
        total_product *= number

    return {"sum": total_sum, "product": total_product}


"""
Time Complexity: O(n)
Space Complexity: O(1)
Optimal Time Complexity: O(n)
"""
