/**
 * Finds common items between two arrays.
 *
 * Time Complexity: We are checking two arrays. If the first array has length n and the second has length m, the time complexity is O(n * m), 
   because filter iterates over the first array and includes scans the second array for each element.
 * Space Complexity: A new Set is created to store unique common items, which in the worst case can be the size of the first array --> O(n).
 * Optimal Time Complexity: By converting one array to a Set, we can check membership in O(1) for each element of the other array, reducing the time complexity to O(n + m).
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const firstArr = new Set(firstArray); //O(n)
  const commons = secondArray.filter((el) => firstArr.has(el)); //O(m)
  return [...new Set(commons)]; // remove duplicates
};
