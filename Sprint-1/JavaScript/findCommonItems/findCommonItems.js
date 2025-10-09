/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n*m) where n and m are length of each array
 * Space Complexity: O(n) where n is a length of arrays
 * Optimal Time Complexity: O(n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  // [...new Set(firstArray.filter((item) => secondArray.includes(item))),]
  // program flow:
  // firstArray.filter go through the each item in first array (loop)
  // secondArray.includes check if that item is in the second array (nested loop)
  // nested loop result in O(n^2) time complexity

  // to reduce time complexity to sublinear on the number of elements in the arrays we can use Set and it's .intersection() method

  // complexity of this operation is O(n)
  const firstArraySet = new Set(firstArray);
  // complexity of this operation is O(m)
  const secondArraySet = new Set(secondArray);
  // intersection method uses has method which is considered to be faster than O(n) and since JS uses hash tables for has methods, the complexity should be
  // has O(1) and intersection O(n) which result in O(n) overall time complexity
  return Array.from(firstArraySet.intersection(secondArraySet));
};
