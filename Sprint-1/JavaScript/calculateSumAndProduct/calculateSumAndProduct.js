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
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(1) - Only using constant extra space
 * Optimal Time Complexity: O(n) - Cannot do better than linear time
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  // OPTIMIZED IMPLEMENTATION: Single pass algorithm
  // Previous implementation used two separate loops (2n operations)
  // This version combines both calculations in one loop (n operations)

  let sum = 0; // O(1) space
  let product = 1; // O(1) space

  // Single pass through array: O(n) time complexity
  for (const num of numbers) {
    sum += num; // O(1) operation per element
    product *= num; // O(1) operation per element
  }

  // Return optimized object syntax: O(1) space
  return { sum, product };
}

/*
 * ORIGINAL IMPLEMENTATION (for comparison):
 *
 * export function calculateSumAndProduct(numbers) {
 *   let sum = 0;
 *   for (const num of numbers) {    // First pass: O(n)
 *     sum += num;
 *   }
 *
 *   let product = 1;
 *   for (const num of numbers) {    // Second pass: O(n)
 *     product *= num;
 *   }
 *
 *   return {                        // Total: O(2n) = O(n) time
 *     sum: sum,                     // O(1) space
 *     product: product,
 *   };
 * }
 *
 * IMPROVEMENTS MADE:
 * 1. Reduced from 2n to n operations (50% fewer iterations)
 * 2. Better cache locality (single pass through memory)
 * 3. Same O(n) time complexity but with better constant factors
 */
