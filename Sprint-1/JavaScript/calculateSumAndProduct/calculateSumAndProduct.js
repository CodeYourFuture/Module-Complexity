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
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 * 
 * It loops twice: Once to compute the sum and Once to compute the product.
 * 
 * Time Complexity

    Let n be the number of elements in numbers.

    Operations:

    First loop: visits each element = O(n)
    Second loop: visits each element again = O(n)
    Even though there are two separate loops, each runs in linear time. Therefor, Time Complexity: O(n)
  Space Complexity

    We're not allocating any new data structures proportional to n.
    Space Complexity: O(1)
    (No extra space used that grows with input size.)
 *
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


// optimal solution

//make it even cleaner by combining both operations into a single loop, like this. But O(n) is the best We can do for time complexity.

export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;

  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return { sum, product};
}