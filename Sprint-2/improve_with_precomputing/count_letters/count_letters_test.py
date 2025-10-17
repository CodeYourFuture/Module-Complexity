import random
import string
import unittest

from count_letters import count_letters

class CommonPrefixTest(unittest.TestCase):
    def test_only_upper(self):
        self.assertEqual(count_letters("ABC"), 3)

    def test_only_lower(self):
        self.assertEqual(count_letters("abc"), 0)

    def test_both(self):
        self.assertEqual(count_letters("aABCbc"), 0)

    def test_mixed(self):
        self.assertEqual(count_letters("aABCbcDEeFGhI"), 4)

    def test_long_string(self):
        s = ""

        only_upper = set("aeiou")
        alphabet = list(set(string.ascii_letters) - only_upper)
        still_to_include = set(letter for letter in alphabet)

        while len(s) < 10000000 or len(still_to_include) > 0:
            next = random.choice(alphabet)
            s += next
            if next in still_to_include:
                still_to_include.remove(next)

        self.assertEqual(count_letters(s), 5)


if __name__ == "__main__":
    unittest.main()
