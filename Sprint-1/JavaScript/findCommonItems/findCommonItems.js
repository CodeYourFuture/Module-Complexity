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
/**
 * Time Complexity (Original): O(N \times M) — The original code used .filter() on the first list and .includes() on the second list. Because .includes() has to look through the second list one item at a time from scratch, it acts like a hidden nested loop. For big lists, this gets incredibly slow.
 * Space Complexity (Improved): O(N + M) — The improved version uses extra memory because it creates two new sets (firstSet and secondSet) to hold the unique items from both lists.
 * Optimal Time Complexity (Improved): O(N + M) — By turning the second list into a Set, the .has() check becomes instant ($O(1)$) instead of scanning the whole list. This makes the entire function run in fast linear time.
 */