/**
 * Remove duplicate values from a sequence, preserving the order
 * of the first occurrence of each value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
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
}

// Time complexity is O(n²) because we use nested loops
// to compare each item with the unique items already found.

// Space complexity is O(n) because we create a new array
// that may store up to n unique items.

// Optimal time complexity is O(n) because using a Set
// allows us to check for duplicates more efficiently.

export function removeDuplicates(inputSequence) {
  const uniqueItems = new Set(inputSequence);

  return [...uniqueItems];
}

// Time complexity: O(n) on average
// Space complexity: O(n)
// Optimal time complexity: O(n)
