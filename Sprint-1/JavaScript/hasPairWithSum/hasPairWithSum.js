/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n^2) - nested loops compare every pair
 * Space Complexity: O(1) - no extra data structures
 * Optimal Time Complexity: O(n) - using a Set to store seen numbers
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    const complement = target - num;
    if (seen.has(complement)) {
      return true;
    }
    seen.add(num);
  }

  return false;
}
