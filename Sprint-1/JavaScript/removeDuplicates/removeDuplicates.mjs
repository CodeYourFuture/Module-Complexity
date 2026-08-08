/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n*n) --> there is a nested loop
 * Space Complexity:0(n)--> we are creating a array
 * Optimal Time Complexity: we can use a new Set to remove all duplicates -->O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from //[1,1,2,2,3,4,5,5]
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueSequence = [...new Set(inputSequence)];
  return uniqueSequence;
}
