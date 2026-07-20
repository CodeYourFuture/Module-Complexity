/**
 * Calculate the sum and product of integers in a list.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * The original solution used two separate loops.
 * This version combines both calculations into a single loop,
 * reducing the number of iterations while keeping constant memory usage.
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing the sum and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum,
    product,
  };
}
