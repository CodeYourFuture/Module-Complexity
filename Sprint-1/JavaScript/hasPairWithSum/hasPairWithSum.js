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

//My Analysis Result
// Time Complexity - since it have two nested loop of the same size/growth here i have a growth of O(n * n) = O(n**2) .. quadratic growth
// Space Complexity - I didnt see any assigning/modifying stored data scenario so i think the space complexity is just O(1) for the return statement
//The inefficiency of this program is due to the nested loop : it creates redudndant checks to compare the numbers.

//here is the refactored code avoiding that redundancy

export function hasPairWithSum(numbers, target) {
  const seenNumbers = new Set();
  for (const num of numbers) {
    const complement = target - num;
    if (seenNumbers.has(complement)) {
      return true; // We found a pair!
    }
    seenNumbers.add(num);
  }
  return false;
}
//here time complexity is reduced to optimal level . just one loop which is O(n)
//for the space complexity here i have O(n) as well because of the Set() i used.
//i traded space to have an optimal time complexity
