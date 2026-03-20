/**
 * Finds common items between two arrays.
 *
 * Areas of inefficiency in original version:
 * - `secondArray.includes(item)` is O(m) and was called for each item in firstArray (n)
 *   resulting in O(n * m) worst-case time.
 *
 * Time Complexity: O(n + m) average
 * Space Complexity:  O(m)
 * Optimal Time Complexity:  O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const setB = new Set(secondArray);

  return [...new Set(firstArray.filter(item => setB.has(item)))];
};