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
