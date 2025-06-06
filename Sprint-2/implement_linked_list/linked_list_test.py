import unittest

from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def test_pushes_then_pops(self):
        l = LinkedList()
        l.push_head("a")
        l.push_head("b")
        l.push_head("c")

        self.assertEqual(l.pop_tail(), "a")
        self.assertEqual(l.pop_tail(), "b")
        self.assertEqual(l.pop_tail(), "c")

    def test_remove(self):
        l = LinkedList()
        l.push_head("a")
        b = l.push_head("b")
        l.push_head("c")

        l.remove(b)

        self.assertEqual(l.pop_tail(), "a")
        self.assertEqual(l.pop_tail(), "c")

    def test_remove_tail(self):
        l = LinkedList()
        a = l.push_head("a")
        b = l.push_head("b")
        l.remove(a)
        self.assertEqual(l.head, b)
        self.assertEqual(l.tail, b)
        self.assertIsNone(b.next)
        self.assertIsNone(b.previous)


if __name__ == "__main__":
    unittest.main()
