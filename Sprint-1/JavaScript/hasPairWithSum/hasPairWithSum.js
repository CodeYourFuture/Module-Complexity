/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n^2)
 * Space Complexity:O(1)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seenNumbers = new Set();
  for (let i = 0; i < numbers.length; i++) {
    // initial solution iterates twice, having outer and inner loop which gives us a time complexity of O(n**2). To optimise this, using a set to store seen numbers, then check whether the complement(target - number) for each num in the array has been seen and in the set. This gives a complexity of O(n)
    let complement = target - numbers[i];

    if (seenNumbers.has(complement)) {
      return true;
    }
    seenNumbers.add(numbers[i]);
  }
  return false;
}
