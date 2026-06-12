/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: worst O(N!) - factorial
 * Space Complexity: O(numbers.length)
 * Optimal Time Complexity: worth become O(N)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum1(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return true;
      }
    }
  }
  return false;
}

export function hasPairWithSum(numbers, target) {

  for (let i = 0; i < numbers.length; i++) {
    if (numbers.includes(target - numbers[i])) {
      return true;
    }
  }
  return false;
}
