/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n * m)
 * Space Complexity: O(k)---> where k is the number of common items
 * Optimal Time Complexity: O(n + m)
 * Explanation: The function uses the filter method to iterate through each item in the first array and
 * checks if it exists in the second array using the includes method.
 * This results in a time complexity of O(n * m) because for each item in the first array,
 * we are checking against all items in the second array.
 *  The space complexity is O(k) because we are creating a new array to store the common items,
 *  where k is the number of common items found.
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const lookup = new Set(secondArray);
  const result = new Set();
  for (const item of firstArray) {
    if (lookup.has(item)) {
      result.add(item);
    }
  }
  return [...result];
};
