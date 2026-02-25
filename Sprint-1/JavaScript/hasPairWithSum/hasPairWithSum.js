/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²) - since it's a nested loop over the same array. 
 * Space Complexity: O(1) - since there's no other array, set, object that gorws proportionally to the input size, space usage doesn't grow.
 * Optimal Time Complexity: O(n) - 
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return true;
      }
    }
  }
  return false;
}
