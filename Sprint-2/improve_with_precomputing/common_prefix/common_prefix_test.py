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

if __name__ == "__main__":
    unittest.main()
