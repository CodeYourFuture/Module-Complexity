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
// export function removeDuplicates(inputSequence) {
//   const uniqueItems = [];

//   for (
//     let currentIndex = 0;
//     currentIndex < inputSequence.length;
//     currentIndex++
//   ) {
//     let isDuplicate = false;
//     for (
//       let compareIndex = 0;
//       compareIndex < uniqueItems.length;
//       compareIndex++
//     ) {
//       if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
//         isDuplicate = true;
//         break;
//       }
//     }
//     if (!isDuplicate) {
//       uniqueItems.push(inputSequence[currentIndex]);
//     }
//   }

//   return uniqueItems;
// }

export function removeDuplicates(inputSequence) {
  let noDuplicates = [...new Set(inputSequence)];
  return noDuplicates;
}

//  * Time Complexity: O(n)
//  * Space Complexity: O(n)
//  * Optimal Time Complexity: O(n)
