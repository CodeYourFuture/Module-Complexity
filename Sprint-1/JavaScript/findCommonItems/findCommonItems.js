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
export const findCommonItems = (firstArray, secondArray) => {
  if (!firstArray || !secondArray) return [];

  // remove all duplicates
  const firstSet = new Set(firstArray);
  const secondSet = new Set(secondArray);

  const common = [...firstSet].filter((item) => secondSet.has(item));

  return common;
};
// a normal list can have same item many time 
// we use new Set to remove dublicates for both arrays
// because we cleaned firat array , the computer never check same word twice, same for second array
// filter works with normal arrays so we spred firstSet to look like array
// we put if statement if eaither one is empty it doesnt crash
