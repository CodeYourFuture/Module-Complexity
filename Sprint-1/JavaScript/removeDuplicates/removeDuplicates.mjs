/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: Quadratic
 * nested loop
 * Space Complexity: O(N)
 * Optimal Time Complexity:O(N)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
	const uniqueItems = [];

	// for (
	//   let currentIndex = 0;
	//   currentIndex < inputSequence.length;
	//   currentIndex++
	// ) {
	//   let isDuplicate = false;
	//   for (
	//     let compareIndex = 0;
	//     compareIndex < uniqueItems.length;
	//     compareIndex++
	//   ) {
	//     if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
	//       isDuplicate = true;
	//       break;
	//     }
	//   }
	//   if (!isDuplicate) {
	//     uniqueItems.push(inputSequence[currentIndex]);
	//   }
	// }
	const itemsWeChecked = {};
	for (const item of inputSequence) {
		if (!itemsWeChecked[item]) {
			uniqueItems.push(item);
			itemsWeChecked[item] = true;
		}
	}

	return uniqueItems;
}
