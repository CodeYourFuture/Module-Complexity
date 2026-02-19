import {hasPairWithSum} from "./hasPairWithSum.js";
import assert from "node:assert/strict";

console.log("Testing hasPairWithSum...");

// Test when pair exists
assert.strictEqual(
  hasPairWithSum([5, 2, 8, 1, 9], 10),
  true,
  "Should find pair summing to 10"
);
assert.strictEqual(
  hasPairWithSum([1, 2, 3, 4], 7),
  true,
  "Should find pair summing to 7"
);

// Test when pair doesn't exist
assert.strictEqual(
  hasPairWithSum([5, 2, 8, 1, 9], 12),
  false,
  "Should return false when no pair sums to target"
);

// Test edge case - empty array
assert.strictEqual(hasPairWithSum([], 5), false, "Should handle empty array");

console.log("✓ All hasPairWithSum tests passed!");
