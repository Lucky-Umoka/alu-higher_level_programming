#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with a list of ascending integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test with a list of descending integers."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list, should return None."""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Test with no argument passed, should return None."""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-5, 0, 5]), 5)

    def test_duplicate_max(self):
        """Test with duplicate maximum values in the list."""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)

    def test_float_numbers(self):
        """Test with a list of float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
