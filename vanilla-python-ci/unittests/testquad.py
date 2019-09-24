#!/usr/bin/env python
"""Unit tests using unittest"""

import unittest
import sys
sys.path.append('../')
from main import calc_square


class MyTests(unittest.TestCase):
    """Define class from unittest"""
    def setUp(self):
        """Use setUp from unittest"""
        self.val = 3
    def test_square(self):
        """Define test function starting with test_"""
        val2 = calc_square(self.val)
        self.assertTrue(val2 == 9)

if __name__ == '__main__':
    unittest.main()
