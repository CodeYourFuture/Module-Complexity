/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * The complexity can be reduced from O(n^2) to O(n) by using a Set to track seen items,
 * instead od searching through the entire UniqueItems array each time , we can check a Set in 0(1) time
 * 
 * Time Complexity: 0(n) Single pass through array and O(1) for Set lookups, resulting in O(n) overall
 * Space Complexity: 0(n) Set and array both store up to n unique elements 
 * Optimal Time Complexity: 0(n) - We must examine each element at least once to determine if it's a duplicate, so O(n) is the best we can achieve for this problem.
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
