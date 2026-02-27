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
 * Time Complexity: O(n) - We go through the list only once. The previous code had two loops (2n), but now we do everything in one loop (n).
 * Space Complexity: O(1) - We represent the result with just two variables (sum and product), so we don't use extra memory.
 * Optimal Time Complexity: O(n) - We have to look at every number at least once, so we can't be faster than O(n).
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  // Refactor: Instead of looping twice, I calculate both sum and product in the same loop.
  // This is better because we only loop through the list once.
  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}
