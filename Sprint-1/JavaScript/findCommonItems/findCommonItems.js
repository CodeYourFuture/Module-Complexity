/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n + m)
 * The old code used .includes() inside .filter(), which meant a loop inside a loop (O(n^2)).
 * By using a 'Set', we can check if an item exists instantly (O(1)).
 *
 * Space Complexity: O(n) - We create a Set to store the items from the first array.
 *
 * Optimal Time Complexity: O(n) - We must look at every item at least once to compare them.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  // Refactor: I put the first array into a Set for fast checking.
  const itemsInFirst = new Set(firstArray);
  const commonItems = new Set();

  for (const item of secondArray) {
    // Checking 'itemsInFirst.has(item)' is very fast O(1).
    // The old 'includes()' was slow because it searched the whole list O(n).
    if (itemsInFirst.has(item)) {
      commonItems.add(item);
    }
  }

  // Convert the Set back to an array to return it
  return [...commonItems];
};