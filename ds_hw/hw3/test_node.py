import unittest

from node import *


class NodeTestCase(unittest.TestCase):
    def setUp(self):
        self._node = Node(5.5, 3)

    def test_construct(self):
        self.assertAlmostEqual(5.5, self._node.coefficient)
        self.assertEqual(3, self._node.exponent)

    def test_set_data(self):
        self._node.set_data(6.1, 4)
        self.assertAlmostEqual(6.1, self._node.coefficient)
        self.assertEqual(4, self._node.exponent)

    def test_set_coefficient(self):
        self._node.coefficient = 6.1
        self.assertAlmostEqual(6.1, self._node.coefficient)
        self.assertEqual(3, self._node.exponent)

    def test_set_exponent(self):
        self._node.exponent = 4
        self.assertAlmostEqual(5.5, self._node.coefficient)
        self.assertEqual(4, self._node.exponent)

    def test_set_next(self):
        self._node.next = Node(3, 5)
        next_node = self._node.next
        self.assertAlmostEqual(3, next_node.coefficient)
        self.assertEqual(5, next_node.exponent)

    def test_eq(self):
        self.assertTrue(Node(5.5, 3) == self._node)
        self.assertFalse(Node(5.5, 2) == self._node)
        self.assertFalse(Node(0.5, 3) == self._node)
        self.assertFalse(Node(3.1, 5) == self._node)

    def test_ne(self):
        self.assertFalse(Node(5.5, 3) != self._node)
        self.assertTrue(Node(5.5, 2) != self._node)
        self.assertTrue(Node(0.5, 3) != self._node)
        self.assertTrue(Node(3.1, 5) != self._node)

    def test_add(self):
        self.assertEqual(Node(6.6, 9), Node(3.1, 9) + Node(3.5, 9))

    def test_sub(self):
        sub_node = Node(3.1, 9) - Node(3.5, 9)
        self.assertAlmostEqual(-0.4, sub_node.coefficient)
        self.assertAlmostEqual(9, sub_node.exponent)

    def test_mul(self):
        self.assertEqual(Node(10, 6), Node(5, 4) * Node(2, 2))
        self.assertEqual(Node(-10, 6), Node(5, 4) * Node(-2, 2))
        self.assertEqual(Node(-10, 6), Node(-5, 4) * Node(2, 2))
        self.assertEqual(Node(10, 6), Node(-5, 4) * Node(-2, 2))

    def test_truediv(self):
        self.assertEqual(Node(5, 4), Node(10, 6) / Node(2, 2))
        self.assertEqual(Node(-5, 4), Node(-10, 6) / Node(2, 2))
        self.assertEqual(Node(-5, 4), Node(10, 6) / Node(-2, 2))
        self.assertEqual(Node(5, 4), Node(-10, 6) / Node(-2, 2))


if __name__ == '__main__':
    unittest.main()
