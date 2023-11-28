#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test max_integer with an unordered list"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        result = max_integer([-1, -5, -3, -2])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative numbers"""
        result = max_integer([-1, 5, -3, 2])
        self.assertEqual(result, 5)
