import {hasPairWithSumSorted} from "./hasPairWithSumSorted.js";
import assert from "node:assert/strict";

console.log("Testing hasPairWithSumSorted...");

// Test when pair exists
assert.strictEqual(
  hasPairWithSumSorted([5, 2, 8, 1, 9], 10),
  true,
  "Should find pair summing to 10"
);
assert.strictEqual(
  hasPairWithSumSorted([1, 2, 3, 4], 7),
  true,
  "Should find pair summing to 7"
);

// Test when pair doesn't exist
assert.strictEqual(
  hasPairWithSumSorted([5, 2, 8, 1, 9], 12),
  false,
  "Should return false when no pair sums to target"
);

// Test edge case - empty array
assert.strictEqual(
  hasPairWithSumSorted([], 5),
  false,
  "Should handle empty array"
);

// Test with unsorted input
assert.strictEqual(
  hasPairWithSumSorted([9, 1, 4, 2, 6], 8),
  true,
  "Should work with unsorted input"
);

console.log("✓ All hasPairWithSumSorted tests passed!");
