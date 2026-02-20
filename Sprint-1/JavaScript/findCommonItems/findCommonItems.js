/**
 * Finds common items between two arrays.
 *
 * Time Complexity: Logarythmic? No Quadratic
 *
// nested so includes loops over each item in first arr
// nested loops are not efficient and used filter and inlcudes
//array.inlcudes method goes item by item
 * Space Complexity: O(N)
 * Optimal Time Complexity: o(N)?
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
	//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
	const dictToCheck = {};
	const doubled = [];

	for (const item of firstArray) {
		dictToCheck[item] = true;
	}

	for (const item of secondArray) {
		if (dictToCheck[item]) {
			doubled.push(item);
			dictToCheck[item] = false;
		}
	}
	return doubled;
};
