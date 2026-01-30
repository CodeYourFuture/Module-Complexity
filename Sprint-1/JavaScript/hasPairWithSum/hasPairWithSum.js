/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n) - nested loops 
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seenNumbers = new Set();

  for (const num of numbers) {
    const match = target - num;
    if (seenNumbers.has(match)) {
      return true;
    }
    seenNumbers.add(num);
  }
  return false;
}
