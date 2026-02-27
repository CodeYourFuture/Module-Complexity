/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:before refactoring O(n²)- after refactoring O(n)
 * Space Complexity:before refactoring O(1)- after refactoring O(n)
 * Optimal Time Complexity:O(n)
 * https://www.hellointerview.com/learn/code/two-pointers/overview
 * The refactored solution iterates through the array once and uses a hash-based
 * data structure (Set) to keep track of previously seen numbers.
 * For each number, it checks whether the complement (target - current number)
 * already exists in the Set. If it does, a valid pair has been found.
 * This approach avoids sorting and achieves linear time complexity.
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];
    if (seen.has(target - num)) {
      return true;
    } else {
      seen.add(num);
    }
  }
  return false;
}
