/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(N*N) quadratic
 * Space Complexity: O(N)
 * Optimal Time Complexity: become O(N)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueItems = new Set();
  inputSequence.forEach((element) => {
    uniqueItems.add(element)
  });

  return [...uniqueItems];
}
