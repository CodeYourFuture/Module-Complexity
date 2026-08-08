/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:  O(n²) original, O(n) optimised using Set
 * Space Complexity: O(n) for 2 options
 * Optimal Time Complexity: O(n) linear time is the best possible
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
    const seenItems = new Set();
    const uniqueSequence = [];

    for (const item of inputSequence) {
        if (!seenItems.has(item)) {
            seenItems.add(item);
            uniqueSequence.push(item);
        }
    }

    return uniqueSequence;
}

