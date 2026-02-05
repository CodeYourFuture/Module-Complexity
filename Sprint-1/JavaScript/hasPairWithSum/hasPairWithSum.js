/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n)
 * The old code used nested loops (loop inside a loop) which is slow O(n^2).
 * I used a Set to remember the numbers we have seen. This lets us find the answer in one loop O(n).
 * 
 * Space Complexity: O(n) - We use a Set to store the numbers we have visited.
 * Optimal Time Complexity: O(n) - We need to check the numbers at least once to find the pair.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  // Refactor: I used a Set to store numbers we have already seen.
  const seenNumbers = new Set();

  for (const num of numbers) {
    // Calculate what number we need to reach the target.
    // Example: If target is 10 and num is 3, we need 7.
    const match = target - num;

    // Check if the number we need is already in our Set.
    // .has() is very fast O(1).
    if (seenNumbers.has(match)) {
      return true;
    }

    // Add the current number to the Set so we can use it later.
    seenNumbers.add(num);
  }
  
  return false;
}
