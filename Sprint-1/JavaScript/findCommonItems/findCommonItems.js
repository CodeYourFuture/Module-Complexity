/**
 * Finds common items between two arrays.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
// export const findCommonItems = (firstArray, secondArray) => [
//   ...new Set(firstArray.filter((item) => secondArray.includes(item))),
// ];

export const findCommonItems = (firstArray, secondArray) => {
  let firstArr = new Set(firstArray);
  let secondArr = new Set(secondArray);

  return [...firstArr].filter((arr) => secondArr.has(arr));
};

//  * https://www.w3schools.com/js/js_set_methods.asp#mark_set_new
//  * Time Complexity: O(m+n)
//  * Space Complexity: O(m+n)
//  * Optimal Time Complexity: O(m+n)
