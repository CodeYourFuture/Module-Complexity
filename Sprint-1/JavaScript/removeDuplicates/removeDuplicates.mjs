/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: is O(n^2) coz it used nested loop to remove the duplications 
 * Space Complexity: it is O(n) coz it is grows directly proportional with the input size 
 * Optimal Time Complexity: to O(n) - because even if i'm using Set, i need to go through each element in the array, which leads me to the time complexity will be growing directly proportional with the input size
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueItems = [...new Set(inputSequence)]

  return uniqueItems;
}

console.log(removeDuplicates([5, 2, 2, 3, 4, 4, 1]))
console.log(removeDuplicates(["a", "e", "b", "a", "c", "c", "a"])) 
