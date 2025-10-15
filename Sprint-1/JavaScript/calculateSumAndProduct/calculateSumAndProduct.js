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

//My Analysis report
// the function have  two loops which looks similar and can be simplified, they makes the time complexity of the function
// a numbers.length times which is O(n). for the two loops time complexity becomes O(n) + O(n) = O(2n)
// after looping it stores the results on the two variables i.e. sum and product which have O(1) + O(1) space complexity.
// the space complexity related to arr size is unavoidable/ unchangeable and is optimal in this case , which is O(n)
// And The area of inefficiency for this code is on the loop (i.e. looping twice)

//refactored code for better efficiency.
//what i have done here is i use a single loop to change the efficiency from o(2n) to o(n)

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
