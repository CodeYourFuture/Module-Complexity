/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
  * Time Complexity: o(n2) the function use 2 nested loop
 * Space Complexity:o(1)no additional significant memory used
 * Optimal Time Complexity:  O(n) — in the refactored version using a Set for lookups
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
//The original version used two nested loops, meaning it checked every possible pair of numbers in the array to see if they added up to the target. This approach has a time complexity of O(n²), which becomes very slow as the list grows larger.
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
