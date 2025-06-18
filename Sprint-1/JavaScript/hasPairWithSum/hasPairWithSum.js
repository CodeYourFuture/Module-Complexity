/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²) original version used a nested loop to check all pairs
 * Space Complexity: O(1) no extra space used in the original version
 * Optimal Time Complexity: O(n) — in the refactored version using a Set for lookups
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

// My solution -  Refactored to use a Set for faster lookup, reducing time from O(n²) to O(n) 
export function hasPairWithSum(numbers, target) {
    const previousNumbers = new Set();

    for (const num of numbers) {
        const neededValue = target - num;
        if (previousNumbers.has(neededValue)) {
            return true;
        }
        previousNumbers.add(num);
    }

    return false;
}

