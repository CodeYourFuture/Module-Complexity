/**
 * Find if there is a pair of numbers that sum to target (Sorted version)
 * Time Complexity:
 * Space Complexity:
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} targetSum - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSumSorted(numbers, targetSum) {
  // Create sorted copy to avoid modifying input
  const sortedNumbers = [...numbers].sort(
    (firstNumber, secondNumber) => firstNumber - secondNumber
  );

  for (
    let currentIndex = 0;
    currentIndex < sortedNumbers.length;
    currentIndex++
  ) {
    const requiredMatch = targetSum - sortedNumbers[currentIndex];

    for (
      let searchIndex = currentIndex + 1;
      searchIndex < sortedNumbers.length;
      searchIndex++
    ) {
      if (sortedNumbers[searchIndex] === requiredMatch) {
        return true;
      }
      // Early exit if we've gone too far
      if (sortedNumbers[searchIndex] > requiredMatch) {
        break;
      }
    }
  }
  return false;
}
