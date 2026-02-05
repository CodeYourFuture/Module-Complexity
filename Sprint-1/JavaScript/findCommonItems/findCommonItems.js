/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(N + M)
 * Space Complexity: O(M)
 * Optimal Time Complexity: O(N + M)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  // 1. Create a Set from the second array. (O(M) time)
  // This allows for O(1) average time lookups using the has() method,
  // as per the typical performance characteristics of Set.
  const secondSet = new Set(secondArray);

  // 2. Filter the first array (O(N) time) using O(1) lookups.
  // The filter uses Set.prototype.has() for O(1) average time complexity.
  // The overall time complexity for the filter step becomes O(N * 1) = O(N).
  const commonItems = firstArray.filter((item) => secondSet.has(item));

  // 3. Use a final Set to guarantee unique results (O(N) time) and return an array.
  return [...new Set(commonItems)];
};

/*
Explanation:
The function first creates a Set from the second array, which takes O(M) time,
where M is the length of the second array. This allows for O(1) average time
lookups when checking for common items.

Next, it filters the first array, which takes O(N) time, where N is the length
of the first array. Each lookup in the Set is O(1) on average, so the overall
time complexity for this step remains O(N).

Finally, to ensure that the result contains only unique items, a new Set is
created from the filtered results, which also takes O(N) time in the worst case.
Converting this Set back to an array is also O(N).

Overall, the total time complexity is O(N + M), which is optimal for this problem,
as each element from both arrays must be examined at least once.

Space Complexity:
The space complexity is O(M) due to storing the second array in a Set.
The additional space used for the result array is O(K), where K is the number
of unique common items, but this is typically less than or equal to M.

Source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
*/