/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Areas of inefficiency in original version:
 * - Nested loop: for each element in inputSequence, it scanned uniqueItems so far.
 *   That creates quadratic behavior in the worst case.
 * 
 * Time Complexity: O(n²)
 * Space Complexity:O(n)
 * Optimal Time Complexity:
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
