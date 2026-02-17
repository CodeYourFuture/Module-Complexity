/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 * "sum": 10, // 2 + 3 + 5
 * "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(N)
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  // The complexity is reduced by combining the two sequential O(N) loops
  // into a single O(N) loop, cutting the number of array traversals in half.
  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
    sum: sum,
    product: product,
  };
}

/* Explanation:
   The complexity is reduced by combining the two sequential O(N) loops
   into a single O(N) loop, cutting the number of array traversals in half.

   Complexity of Refactor
   Time Complexity: O(N)(Linear Time). 
   The function performs only one pass over the $N$ elements of the array, 
   which is the most efficient possible time complexity for this problem, 
   as every element must be read once.
   
   Space Complexity: O(1)(Constant Time). 
   Only a fixed number of variables (sum, product, and num) are used, 
   regardless of the size of the input array.
*/