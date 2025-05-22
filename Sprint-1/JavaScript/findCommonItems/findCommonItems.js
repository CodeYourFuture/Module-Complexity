/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n^3): we effectively have three nested loops - the first over first_sequence, the second over second_sequence, and the third in the "not in" check which may contain the same number of elements as either of the sequences.
 * Space Complexity: O(n): in the case of complete overlap we may store all of the elements from the sequences in common_items.
 * Optimal Time Complexity: We could optimise this to O(n) by using data structures with O(1) insertion and contains look-up.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const overlap = new Set();
  const secondSet = new Set(secondArray);
  for (const element of firstArray) {
    if (secondSet.has(element)) {
      overlap.add(element);
    }
  }
  return [...overlap];
};
