/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:To using nested loop for compare elements time complexity will be ---> O(n*n)
 * Space Complexity:We only use few variables -->O(1)
 * Optimal Time Complexity:Iterate array only once and use a Set for O(1) lookups / total----->O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();
  for (let i = 0; i < numbers.length; i++) {
    const neededNumber = target - numbers[i];
    if (seen.has(neededNumber)) {
      return true;
    } else {
      seen.add(numbers[i]);
    }
  }
  return false;
}
