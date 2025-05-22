/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n^2) - Two nested loops, each looking over worst-case the whole input list.
 * Space Complexity: O(n) - Stores the overlapping items, which may be proportional to all of them.
 * Optimal Time Complexity: O(n) - If we use a data structure with O(1) insertion and contains-look-up to track which elements have already been seen.
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueItems = new Set();

  for (const item of inputSequence) {
    uniqueItems.add(item);
  }
  return [...uniqueItems];
}
