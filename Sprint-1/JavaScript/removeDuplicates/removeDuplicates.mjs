/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n**2)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const seenItems = new Set();
  let result = [];
  // The initial solution was a nested loop, with a time complexity of O(n**2). This was optimised by using a set to track seen items, thereby reducing the complexity to O(n)
  for (const item of inputSequence) {
    if (!seenItems.has(item)) {
      seenItems.add(item);
      result.push(item);
    }
  }
  return result;
}
