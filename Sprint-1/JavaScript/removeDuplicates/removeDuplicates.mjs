/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 * Explanation: The function checks each element against all previously seen elements to determine,
 * if it is a duplicate, resulting in a time complexity of O(n²) in the worst case.
 * The space complexity is O(n) because we are storing unique items in a new array.
 *  The optimal time complexity can be achieved by using a Set to track seen items,
 * which allows for O(1) average time complexity for lookups, resulting in an overall time complexity of O(n).
 * Refactor: Using Set allows to constant-time membership checks, which significantly reduces the time complexity from O(n²) to O(n).
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
