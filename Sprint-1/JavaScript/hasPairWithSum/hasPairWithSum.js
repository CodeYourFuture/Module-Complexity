/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:
 *      ANSWER: O(n)
        Because the array is looped through once.
        
 * Space Complexity:
        ANSWER: O(n)
        Because a Set is used to store seen numbers.

 * Optimal Time Complexity:
        ANSWER: O(n)
        Each number is processed once using a Set for lookup.
 *

    Original Time Complexity: O(n^2)
    
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    const complement = target - num;

    if (seen.has(complement)) {
      return true;
    }

    seen.add(num);
  }
  

  return false;
}
