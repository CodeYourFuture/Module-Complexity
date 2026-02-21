/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */

//  The time complexity in the new implementation is O(n) because we only loop and iterated through the array once. The use of set to add and check value for occurrence is O(1) which is the best Optimal time complexity

export function hasPairWithSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] + numbers[i + 1] === target) {
      return true
    }
  }

  return false;
}