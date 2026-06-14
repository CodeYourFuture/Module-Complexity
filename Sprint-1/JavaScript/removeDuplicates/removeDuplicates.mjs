/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  // put items in a Set to remove duplicates, then make it back into an array
  return [...new Set(inputSequence)];
}

// the old code uses a loop inside a loop. Because it multiplies the work, it gets slower and slower the bigger your list grows
/**
 * Time Complexity (Original): O(N^2) — The original code used a loop inside a loop (currentIndex and compareIndex) to scan through the growing uniqueItems list for every item. This made it very slow for larger inputs.
 * Space Complexity (Improved): O(N) — The improved version uses extra memory to create a temporary Set and build the new unique array.
 * Optimal Time Complexity (Improved): O(N) — By using a Set, the computer instantly filters out all duplicates in a single pass through the data, making it incredibly fast.
 */
