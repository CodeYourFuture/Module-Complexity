"""
Calculate the sum and product of integers in a list
Note: the sum is every number added together
and the product is every number multiplied together
so for example: [1, 2, 3, 4] would return
{
    "sum": 10, // 1 + 2 + 3 + 4
    "product": 24 // 1 * 2 * 3 * 4
}
Time Complexity: 
Space Complexity: 
"""
from typing import List, Dict

def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
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