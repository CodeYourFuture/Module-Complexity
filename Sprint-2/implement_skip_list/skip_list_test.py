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

    def test_duplicate_values(self):
        """Test that duplicate values are handled correctly"""
        sl = SkipList()
        
        # Insert duplicates
        sl.insert(5)
        sl.insert(2)
        sl.insert(5)
        sl.insert(2)
        sl.insert(5)
        
        # All duplicates should be in the list and sorted
        self.assertEqual(sl.to_list(), [2, 2, 5, 5, 5])
        
        # Check membership for duplicates
        self.assertIn(2, sl)
        self.assertIn(5, sl)
        
        # Verify non-existent values
        self.assertNotIn(1, sl)
        self.assertNotIn(3, sl)
        self.assertNotIn(6, sl)

    def test_large_random_inserts(self):
        """Test with larger dataset and random insertion order"""
        sl = SkipList()
        
        # Insert numbers in random order
        numbers = [7, 3, 9, 1, 8, 2, 6, 4, 10, 5]
        for num in numbers:
            sl.insert(num)
        
        # Should be sorted regardless of insertion order
        self.assertEqual(sl.to_list(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
        # Verify all numbers are found
        for num in range(1, 11):
            self.assertIn(num, sl)
        
        # Verify numbers outside range are not found
        self.assertNotIn(0, sl)
        self.assertNotIn(11, sl)
        self.assertNotIn(15, sl)



if __name__ == "__main__":
    unittest.main()
