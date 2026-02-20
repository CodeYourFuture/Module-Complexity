/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:Quadratic time
 * nested loop so inefficient comparing of each i j to target
 * Space Complexity: O(N)
 * Optimal Time Complexity: O(N)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
// export function hasPairWithSum(numbers, target) {
// we are now making a cake from cake slices
// numbers are now slices of cake and target is a a number of slices taht makes a whole cake

export function hasPairWithSum(slices, targetWholeCake) {
	// for (let i = 0; i < numbers.length; i++) {
	//   for (let j = i + 1; j < numbers.length; j++) {
	//     if (numbers[i] + numbers[j] === target) {
	//       return true;
	//     }
	//   }
	// }
	const inventoryOfSlices = {};

	for (const slice of slices) {
		const missingPieces = targetWholeCake - slice;

		if (inventoryOfSlices[missingPieces]) {
			return true;
		}

		inventoryOfSlices[slice] = true; // add slice
	}
	return false;
}
