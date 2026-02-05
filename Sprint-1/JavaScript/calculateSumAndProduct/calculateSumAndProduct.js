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
 * Time Complexity:O(2n) originally have this as using 2 separate loops
 * Space Complexity:O(1) no extra space used that rows with input
 * Optimal Time Complexity:O(n) must at least visit each number once
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  //only one loop needed to calculate both sum and product
  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {sum, product};
}
