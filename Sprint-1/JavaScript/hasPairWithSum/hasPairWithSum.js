/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Initial Time Complexity: O(n²) [nested loops]
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n) [with Set]
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    if (seen.has(target - num)) {
      return true;
    }
    seen.add(num);
  }

  return false;
}
