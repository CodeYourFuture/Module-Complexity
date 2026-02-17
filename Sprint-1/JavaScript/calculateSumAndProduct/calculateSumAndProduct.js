/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity: First and Second loop both iterate through all n elements to calculate sum and product,
 * O(n) + O(n) = O(2n) = O(n), Two sequential passes through the array
 * Space Complexity: O(1), Only a constant amount of space is used for the sum and product variables, regardless of input size
 * Optimal Time Complexity: O(n) - We must examine each element at least once to calculate the sum and product, so O(n) is the best we can achieve for this problem.
 *
 * we can reduce the constant factor by eliminating the redundant second loop
 * Instead of two passes (2n operations), we can do both calculations in a single pass (n operations)
 * 
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  
  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}
