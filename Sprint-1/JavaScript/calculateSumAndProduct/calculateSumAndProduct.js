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
 * Time Complexity: O(2n) - Since we're looping through 2 separate loops
 * Space Complexity: O(1) - only 2 variables used
 * Optimal Time Complexity: O(n) - JS engine must read each number at least once
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */

// export function calculateSumAndProduct(numbers) {
//   let sum = 0;
//   for (const num of numbers) {
//     sum += num;
//   }

//   let product = 1;
//   for (const num of numbers) {
//     product *= num;
//   }

//   return {
//     sum: sum,
//     product: product,
//   };
// }

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
