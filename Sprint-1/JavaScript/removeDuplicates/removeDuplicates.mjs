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


// My Analysis Result
// Time Complexity- It has a nested loop structure, giving it a growth of O(n * n) = O(n²). quadratic growth.
// Space Complexity- A new array 'uniqueItems' is created which can grow up to the size of the input, making the space complexity O(n).
// The inefficiency of this program is due to the nested loop: 
// for every item, it slowly rescans the results to check for duplicates.

//refactored code
export function removeDuplicates(inputSequence) {
  return [...new Set(inputSequence)];
}
// Here the time complexity is reduced to an optimal level O(n).
// For the space complexity, I have O(n) as well because the new Set can store up to n unique items.