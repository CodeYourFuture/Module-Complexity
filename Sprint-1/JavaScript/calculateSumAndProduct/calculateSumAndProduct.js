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
 * Time Complexity: is o(n) - coz only we have one input that needs at least one loop 
 * Space Complexity: here the space is o(1) coz the memory will not growing whatever happen with input 
 * Optimal Time Complexity: here even when i drop one of the loops the optimal time complexity will be still O(n) because we dealing with input need at least one loop
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  for (const num of numbers) {
    sum += num;
    product *= num
  }

  return {
    sum: sum,
    product: product,
  };
}


console.log(calculateSumAndProduct([2, 3, 8, 9]));
