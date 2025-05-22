/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n^2): two nested loops both iterating across the input numbers.
 * Space Complexity: O(1): uses only constant extra storage (to do an addition).
 * Optimal Time Complexity: We can optimise this to O(n) by pre-computing a set of the numbers (O(n)), and for each number (O(n)) checking to see if the corresponding number is in the set (O(1)).
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const numberSet = new Set(numbers);

  for (const number of numbers) {
    if (numberSet.has(target - number)) {
      return true;
    }
  }
  return false;
}
