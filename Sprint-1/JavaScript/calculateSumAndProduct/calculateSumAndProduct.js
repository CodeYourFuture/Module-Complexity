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
 * Time Complexity:O(n)
 * Space Complexity:o(1)
 * Optimal Time Complexity:o(n)
 *The original implementation used two separate loops.
 *This refactor combines them into a single loop to reduce
 *the constant factor, while maintaining the same Big-O complexity.
 
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  for (const num of numbers) {
    product *= num;
    sum += num;
  }

  return {
    sum: sum,
    product: product,
  };
}
