/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
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

// To solve this problem I used this source: https://medium.com/@bloodturtle/finding-pairs-in-an-array-that-sum-to-a-target-value-b553e8c357bb

export function hasPairWithSum(numbers, target) {
  let seen = new Set();
  for (let num of numbers) {
    let complement = target - num;
    if (seen.has(complement)) {
      return true;
    }
    seen.add(num);
  }
  return false;
}

//  * Time Complexity: O(n)
//  * Space Complexity: O(n)
//  * Optimal Time Complexity: O(n)
// This solution is optimal because it uses a hash set(based on hash table logic) for constant-time lookups and processes each element once.
