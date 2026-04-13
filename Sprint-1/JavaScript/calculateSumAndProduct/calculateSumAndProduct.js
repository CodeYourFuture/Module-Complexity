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
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 * Explanation: The function iterates through the list of numbers twice,
 *  once to calculate the sum and once to calculate the product. 
 * Each iteration takes O(n) time, resulting in a total time complexity of O(n). 
 * The space complexity is O(1) because we are using a constant amount of space to store the sum and product, 
 * regardless of the size of the input list.
 * 
 * Refactor:
 * I combined the two loops into a single loop 
 * to calculate both the sum and product simultaneously.
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

  return {sum,product};
}
