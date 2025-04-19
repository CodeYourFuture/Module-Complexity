import {findCommonItems} from "./findCommonItems.js";
import assert from "node:assert/strict";

console.log("Testing findCommonItems...");

// Test with common elements
assert.deepStrictEqual(
  findCommonItems([10, 20, 30], [20, 30, 40]),
  [20, 30],
  "Should find common numbers"
);

// Test with no common elements
assert.deepStrictEqual(
  findCommonItems(["apple", "banana", "orange"], ["grape", "kiwi", "mango"]),
  [],
  "Should return empty array when no common elements"
);

// Test edge case - empty array
assert.deepStrictEqual(
  findCommonItems([], [1, 2, 3]),
  [],
  "Should handle empty array"
);

// Test with duplicate elements
assert.deepStrictEqual(
  findCommonItems([1, 1, 2, 2], [1, 2, 2]),
  [1, 2],
  "Should handle duplicate elements"
);

console.log("✓ All findCommonItems tests passed!");
