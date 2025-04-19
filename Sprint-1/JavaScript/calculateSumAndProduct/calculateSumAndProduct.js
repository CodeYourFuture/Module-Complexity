/**
 * Calculate the sum and product of integers in a list
 * Time Complexity:
 * Space Complexity:
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  for (const num of numbers) {
    sum += num;
  }

  let product = 1;
  for (const num of numbers) {
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}

/** Note: the "sum" is every number added together
* and the "product" is every number multiplied together
* so for example: [1, 2, 3, 4] would return
* {
   "sum": 10, // 1 + 2 + 3 + 4
   "product": 24 // 1 * 2 * 3 * 4
* } 
*/
