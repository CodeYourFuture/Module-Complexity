/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * Refactor:
 * The original implementation used nested loops to check for duplicates,
 * resulting in O(n²) time complexity. Using a Set allows constant-time
 * lookups while preserving the insertion order of unique values.
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
