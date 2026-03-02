/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Initial Time Complexity: O(n²) [nested loops]
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n) [with Set]
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const seen = new Set();
  const uniqueItems = [];

  for (const item of inputSequence) {
    if (!seen.has(item)) {
      seen.add(item);
      uniqueItems.push(item);
    }
  }

  return uniqueItems;
}
