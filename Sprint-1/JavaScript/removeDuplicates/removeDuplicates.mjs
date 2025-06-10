/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n^2) because we have two nested loops
 * Space Complexity: O(n) uniqueItems array stores up to n elements if all are unique
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
/*export function removeDuplicates(inputSequence) {
  const uniqueItems = [];

  for (
    let currentIndex = 0;
    currentIndex < inputSequence.length;
    currentIndex++
  ) {
    let isDuplicate = false;
    for (
      let compareIndex = 0;
      compareIndex < uniqueItems.length;
      compareIndex++
    ) {
      if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
        isDuplicate = true;
        break;
      }
    }
    if (!isDuplicate) {
      uniqueItems.push(inputSequence[currentIndex]);
    }
  }

  return uniqueItems;
}*/

//Optimal Time Complexity: O(n) we iterate through the inputSequence once

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

