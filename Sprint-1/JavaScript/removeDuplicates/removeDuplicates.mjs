/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: for each element in the input is compared against all previous unique elements: o(n2) 
 * Space Complexity: we store n elements it all elements are unique.
 * Optimal Time Complexity: Each element is processed once O(1).
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const seenItems = new Set();
  const uniqueItems = [];

  for (
    let i = 0;
    i < inputSequence.length;
    i++
  ) {
    const value = inputSequence[i];

    if (!seenItems.has(value)) {
      seenItems.add(value);
      uniqueItems.push(value);
    }
  }

  return uniqueItems;
}
