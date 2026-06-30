/**
 * Finds common items between two arrays.
 *
 * Time Complexity:O(1)
 * Space Complexity:O(n+m)
 * Optimal Time Complexity:O(1)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondArr = new Set(secondArray);

  const uniqueValues = [
    ...new Set(firstArray.filter((item) => secondArr.has(item))),
  ];
  return uniqueValues;
};

console.log(findCommonItems([2, 5, 7], [5, 6, 7]));
