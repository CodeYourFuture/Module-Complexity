/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n)
 * The old code used a nested loop (checking the result array for every item), which is O(n^2).
 * A Set automatically removes duplicates in one go. Converting Array -> Set -> Array takes linear time O(n).
 * 
 * Space Complexity: O(n) - We create a new Set/Array to store the unique items.
 * Optimal Time Complexity: O(n) - We must look at every item at least once to see what it is.
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  // Refactor: I used a Set to remove duplicates automatically.
  // It creates a Set (removes duplicates) and spreads it back into an array.
  return [...new Set(inputSequence)];
}
