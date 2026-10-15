/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * Optimal Time Complexity: O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return true;
      }
    }
  }
  return false;
}

// Time complexity is O(n²) because we use nested loops
// to compare pairs of numbers in the array.

// Space complexity is O(1) because we only use two variables,
// i and j, regardless of the array size.

// Optimal time complexity is O(n) because using a Set
// allows us to find a matching pair in a single loop.

//Improved solution-O(n)
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    const needed = target - num;

    if (seen.has(needed)) {
      return true;
    }

    seen.add(num);
  }

  return false;
}

// Time complexity: O(n)
// Space complexity: O(n)
// Optimal time complexity: O(n)
