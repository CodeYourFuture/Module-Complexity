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
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  for (let i = 0; i < numbers.length; i++) {
    const item = numbers[i];
    sum += item;
    product *= item;
  }

  return { sum, product };
}
// before we had two for loops , imagine numbers is a array of 1,000,000 numbers, then with two for loops it would run 2 milions time 
// now we have one for loop and it will do it one milion times which is half of that

// cleaner and simpler return which does exactly same as before return

// the traditional for loop is faster and simpler for computers

/** Time Complexity (Original): O(N) — The original code uses two separate, back-to-back loops. It loops through the list once for the sum, and then loops through the list a second time for the product.
 * Space Complexity (Improved): O(1) — The improved version uses constant memory. It only stores a few simple number variables (sum, product, and i), which takes up almost no space regardless of how big the list grows.
 * Optimal Time Complexity (Improved): O(N) — The improved version is still linear time, but it is slightly better because it combines everything into a single loop. It does all the math in just one pass through the list. */