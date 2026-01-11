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
  const uniqueItems = [];
  const seen = new Set();

  for (
    let currentIndex = 0;
    currentIndex < inputSequence.length;
    currentIndex++
  ) {
    if (!seen.has(inputSequence[currentIndex])) {
      seen.add(inputSequence[currentIndex]);
      uniqueItems.push(inputSequence[currentIndex])
    }
  }

  return uniqueItems;
}
