/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n) - where n is the length of the input sequence, as we need to iterate through it once to create the Set.
 * Space Complexity: O(n) - in the worst case, if all elements are unique, the Set will contain all elements of the input sequence. so we need memory to store the unique elements.
 * Optimal Time Complexity: O(n)- using a Set to track seen values allows us to achieve linear time complexity for removing duplicates. 
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
 
  return [...new Set(inputSequence)];
}


// approach 2: map and look up object
/*export function removeDuplicates(inputSequence) {
  const seen = {};
  const uniqueItems = [];

  for (const item of inputSequence) {
    if (!seen[item]) {
      seen[item] = true;
      uniqueItems.push(item);
    }
  }

  return uniqueItems;
}*/ 