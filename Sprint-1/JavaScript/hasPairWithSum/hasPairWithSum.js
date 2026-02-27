/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n) where n is the length of the input array. This is because we iterate through the array once to check for pairs, and each lookup in the Set is O(1) on average. The overall time complexity is linear.
 * 
 * 
 * 
 * Space Complexity: O(n) in the worst case, if all numbers in the input array are unique and we end up storing all of them in the Set. The space complexity is linear with respect to the size of the input array.
 * 
 * 
 * 
 * Optimal Time Complexity: O(n) because we need to iterate through the array at least once to check for pairs. The use of a Set allows us to achieve this optimal time complexity by providing constant time lookups for the complement values.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
const seenNumbers = new Set();

for (const num of numbers) {
  const complement = target - num;
  if (seenNumbers.has(complement)) {
    return true;
  }
  seenNumbers.add(num);

}

return false;
} 
console.log(hasPairWithSum([4, 4], 8))
