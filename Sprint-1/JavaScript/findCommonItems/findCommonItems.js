/**
 * Finds common items between two arrays.
 *
 * Time Complexity:O(n * m) because for each element in firstArray, the includes method does a linear search which can take up to m steps, 
 * so that would be O(n*m)
 * 
 * Space Complexity: O(n) beacause firstArray.filter() creates an array of at most n items and Set stores at most n items, 
 * so the overall complexity would be O(n)+O(n) which we consider O(n) as they grow linerly not exponentially
 * 
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
/*export const findCommonItems = (firstArray, secondArray) => [
  ...new Set(firstArray.filter((item) => secondArray.includes(item))),
];*/

//Optimal Time Complexity: O(n+m+k)

export const findCommonItems = (firstArray, secondArray) => {
  const setSecond = new Set(secondArray); // O(m)
  const seen = new Set();

  for (const item of firstArray) { // )(n)
    if (setSecond.has(item)) {
      seen.add(item);
    }
  }

  return [...seen]; //)(k)
};

// this solution is more optimised as it reduces Time Complexity. The time complexity of the inital function was exponential but now it's linear