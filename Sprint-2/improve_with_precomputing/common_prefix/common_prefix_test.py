import random
import string
import unittest

from common_prefix import find_longest_common_prefix

class CommonPrefixTest(unittest.TestCase):
    def test_finds_longest_common_prefix(self):
        strings = [
            "hello Steve",
            "cheese",
            "hello world",
            "hi",
            "cheddar",
        ]
        self.assertEqual(find_longest_common_prefix(strings), "hello ")

    def test_empty_list(self):
        self.assertEqual(find_longest_common_prefix([]), "")

    def test_single_item_list(self):
        self.assertEqual(find_longest_common_prefix(["hello"]), "")

    def test_no_common_prefix(self):
        strings = ["hi", "bye"]
        self.assertEqual(find_longest_common_prefix(strings), "")

    def test_case_sensitivity(self):
        strings = ["Hello", "hello"]
        self.assertEqual(find_longest_common_prefix(strings), "")

    def test_really_long_list(self):
        strings = []
        for _ in range(1000000):
            strings.append("hello" + "".join(random.choices(string.ascii_lowercase, k=20)))
        common_prefix = find_longest_common_prefix(strings)
        self.assertRegex(common_prefix, "^hello.*$")

    def test_multiple_equal_length_prefixes(self):
        """Test when there are multiple prefixes of the same length"""
        strings = [
            "apple_pie",
            "apple_cider", 
            "banana_split",
            "grape_bread",
            "grape_pie"
        ]
        # Both "apple_" and "grape_" are length 6, either could be returned
        result = find_longest_common_prefix(strings)
        self.assertTrue(result in ["apple_", "grape_"])
        self.assertEqual(len(result), 6)

    def test_identical_strings(self):
        """Test when multiple strings are identical"""
        strings = [
            "identical",
            "different",
            "identical", 
            "identical",
            "another"
        ]
        # The longest prefix is between identical strings: "identical"
        self.assertEqual(find_longest_common_prefix(strings), "identical")


if __name__ == "__main__":
    unittest.main()
