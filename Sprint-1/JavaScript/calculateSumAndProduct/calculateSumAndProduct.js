/**
 * Calculate the sum and product of integers in a list
 *
 * For example: [2, 3, 5] returns
 * {
 *   sum: 10,     // 2 + 3 + 5
 *   product: 30  // 2 * 3 * 5
 * }
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing sum and product
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

// Time complexity is O(n) because we visit each element once.

// Space complexity is O(1) because we use a fixed number of variables,
// regardless of the length of the input array.

// Optimal time complexity is O(n) because every element must be examined
// to guarantee the correct sum and product.
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
