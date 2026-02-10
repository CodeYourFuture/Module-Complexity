/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n x m)
 * Space Complexity: O(n)
 * Optimal Time Complexity:
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => [
  ...new Set(firstArray.filter((item) => secondArray.includes(item))),
];


/*
Time Complexity:

n = firstArray.length
m = secondArray.length

filter() loops over firstArray = O(n)
Inside filter, includes() searches secondArray = O(m)
Combined: O(n x m)
new Set(...) and spreading it: O(k) (where k is number of common items)
Overall Time Complexity: O(n x m)


Space Complexity:

We’re creating temporary arrays and a set, all of which scale with the size of firstArray. 
The overall space complexity is O(n).

*/

// Optimal Solution

export const findCommonItems2 = (firstArray, secondArray) => {
  const set2 = new Set(secondArray);
  return [...new Set(firstArray.filter(item => set2.has(item)))];

};

// now set2.has(item) is O(1) (instead of .includes() which is O(m))

//.has() is a constant-time lookup

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
