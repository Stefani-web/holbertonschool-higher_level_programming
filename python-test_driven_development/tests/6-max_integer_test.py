#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_type_error(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3, 4])

    if __name__ == '__main__':
        unittest.main()
