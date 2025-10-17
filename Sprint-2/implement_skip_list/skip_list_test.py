import unittest

from skip_list import SkipList

class SkipListTest(unittest.TestCase):
    def test_single_item(self):
        sl = SkipList()
        sl.insert("a")
        self.assertEqual(sl.to_list(), ["a"])
        self.assertIn("a", sl)
        self.assertNotIn("b", sl)

    def test_general_usage(self):
        sl = SkipList()
        sl.insert(1)
        sl.insert(2)
        sl.insert(3)
        sl.insert(4)
        sl.insert(10)
        sl.insert(5)

        self.assertIn(5, sl)
        self.assertIn(4, sl)
        self.assertNotIn(6, sl)
        self.assertNotIn(7, sl)

        self.assertEqual(sl.to_list(), [1, 2, 3, 4, 5, 10])


if __name__ == "__main__":
    unittest.main()
