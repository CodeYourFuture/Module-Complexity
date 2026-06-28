/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: worst O(N^2) - square
 * Space Complexity: O(1)
 * Optimal Time Complexity: worth become O(N)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */

export function hasPairWithSum(numbers, target) {
  const numbersSet = new Set(numbers);
  const complementsSet = new Set();
  for (let i = 0; i < numbers.length; i++) {
    complementsSet.add(target - numbers[i])
  }
  const intersection = complementsSet.intersection(numbersSet);
  if (intersection.size > 0) return true;
  return false;
}
