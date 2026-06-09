/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(N^2). It takes a loop inside a loop to compare duplicates.
 * Space Complexity: O(N). The uniqueItems array would grow to N in the worst case.
 * Optimal Time Complexity: O(N). It only loops once after optimization. 
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
  return [...new Set(inputSequence)];
}