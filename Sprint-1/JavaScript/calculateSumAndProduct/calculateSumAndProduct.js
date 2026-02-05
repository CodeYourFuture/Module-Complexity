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
 * Time Complexity: O(n) the previous solution iterates through the lists twice, once for the sum and once for the product, but this solution iterates through the list only once, calculating both the sum and product in a single pass. 
  
  
 
 * Space Complexity: O(1) the space complexity is constant because we are using only a fixed amount of space to store the sum and product, regardless of the size of the input list.
 
 * Optimal Time Complexity: O(n) because we need to iterate through all the numbers in the list at least once to calculate the sum and product. so even though the performance improves by reducing the number of iterations, the overall time complexity remains O(n) since we still need to process each element in the list. 
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
