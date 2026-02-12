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
 * Time Complexity: There are two separate loops. Total operation O(n)+O(n) ---> O(n)
 * Space Complexity:We are only using two variables sum and product --->O(1)
 * Optimal Time Complexity:To calculate sum and product, every element must be visited at least once, so the optimal time complexity is O(n)
 * Refactor Note: We can combine both calculations into a single loop for cleaner and more readable code
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
