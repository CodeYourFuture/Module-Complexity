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

