import assert from "node:assert/strict";
import {removeDuplicates} from "./removeDuplicates.mjs";

console.log("Testing removeDuplicates...");

// Test with number duplicates
assert.deepStrictEqual(
  removeDuplicates([5, 2, 2, 3, 4, 4, 1]),
  [5, 2, 3, 4, 1],
  "Should remove duplicate numbers"
);

// Test with string duplicates
assert.deepStrictEqual(
  removeDuplicates(["a", "e", "b", "a", "c", "c", "a"]),
  ["a", "e", "b", "c"],
  "Should remove duplicate strings"
);

// Test edge case - empty array
assert.deepStrictEqual(removeDuplicates([]), [], "Should handle empty array");

// Test with all duplicates
assert.deepStrictEqual(
  removeDuplicates([1, 1, 1, 1]),
  [1],
  "Should handle array with all duplicates"
);

console.log("✓ All removeDuplicates tests passed!");
