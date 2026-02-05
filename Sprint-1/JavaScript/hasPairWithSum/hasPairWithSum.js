/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: o(n2) the function use 2 nested loop
 * Space Complexity:o(1)no additional significant memory used
 * Optimal Time Complexity:  O(n) — in the refactored version using a Set for lookups
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
  const numbersNeeded = new Set(); // stores numbers we've already seen

  for (const num of numbers) {
    const requiredNumber = target - num;
    if (numbersNeeded.has(requiredNumber)) {
      return true; // found a pair!
    }
    numbersNeeded.add(num); // remember current number
  }

  return false; // no pair found
}
