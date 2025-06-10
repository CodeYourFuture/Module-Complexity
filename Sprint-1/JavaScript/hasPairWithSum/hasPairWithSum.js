/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:O(n^2) there are two for loops 
 * Space Complexity: O(1) becuae we are not using any extra space
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
/*export function hasPairWithSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return true;
      }
    }
  }
  return false;
}*/

//Optimal Time Complexity: O(n)

export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) { // O(n)
    const complement = target - num;
    if (seen.has(complement)) {
      return true;
    }
    seen.add(num);
  }

  return false;
}
