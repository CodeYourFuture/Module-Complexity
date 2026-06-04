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
 * Time Complexity:
 *      ANSWER: Because the function loops through the numbers array once,and the running time increases linearly with the size of the input.
 *              O(n). 
 * Space Complexity:
 *      ANSWER: O(1), Because the function only uses two extra variables (sum and product) and does not create any additional data structures based on the input size.
 * 
 
 * Optimal Time Complexity:
            ANSWER: This is optimal because every number in the array must be processed at least once to calculate the sum and product, so it cannot be done faster than O(n).
            O(n) .


   Original Time Complexity: O(2n)
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
