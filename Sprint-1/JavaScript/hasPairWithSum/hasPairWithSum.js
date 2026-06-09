/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(N^2), the loop is inside a loop
 * Space Complexity: O(1). O(i) is for i and j index counters.
 * Optimal Time Complexity: O(N), it loops once after optimization. However, the space complexity becomes O(N) as there is a growing targetSet.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
// export function hasPairWithSum(numbers, target) {
//   for (let i = 0; i < numbers.length; i++) {
//     for (let j = i + 1; j < numbers.length; j++) {
//       if (numbers[i] + numbers[j] === target) {
//         return true;
//       }
//     }
//   }
//   return false;
// }

export function hasPairWithSum(numbers, target) {
  const targetSet = new Set();
  for (let num of numbers) {
    const targetNum = target - num;
    if (targetSet.has(targetNum)) {
      return true;
    } else {
      targetSet.add(num)
    }
  }
  return false;
}