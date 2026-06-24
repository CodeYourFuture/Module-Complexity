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
 * Time Complexity: O(n)
 * Space Complexity:O(1)
 * Optimal Time Complexity:O(n)
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  // Initial code looped twice through the array, i.e. 2 operations (n + n) = O(2n)operations => O(n). Limiting the loop to just one operation makes it n operation => O(n).
  // The space complexity is constant as the variables do not grow when the function is called.

  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}
