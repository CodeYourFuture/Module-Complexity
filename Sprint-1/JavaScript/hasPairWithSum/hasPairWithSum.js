/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 * Explanation: The function uses a nested loop to check every possible pair of numbers in the array
 *  to see if they sum up to the target value.
 * This results in a time complexity of O(n²) because for each number in the array,
 * we are checking it against every other number.
 *The refactored version uses a Set to check for the existence of the complement, reducing the overall complexity to O(n).
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
