/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: 
 *          ANSWER:O(n)
            Because the array is looped through once.
 * Space Complexity:
            ANSWER:O(n)
            Because a Set is used to track seen items.
 * Optimal Time Complexity:
            ANSWER:O(n)
            Each item is processed once using a Set for lookup.
 *
     Original Time Complexity: O(n^2)
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const seen = new Set();
  const result = [];

  for (const item of inputSequence) {
    if (!seen.has(item)) {
      seen.add(item);
      result.push(item);
    }
  }

  return result;
}
