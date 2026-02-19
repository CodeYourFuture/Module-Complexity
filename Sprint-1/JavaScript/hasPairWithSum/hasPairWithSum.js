/**
 * Find if there is a pair of numbers that sum to a given target value.
 *  
 * Areas of inefficiency in original version:
 * - Nested loops compare every possible pair.
 * - This results in quadratic time complexity as input size grows.
 * 
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * - Use a Set to track numbers seen so far.
 * - For each number x, check whether (target - x) has already been seen.
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