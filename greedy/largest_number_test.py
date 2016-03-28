#Uses python3
__author__ = "Shiven"

import unittest
from unittest.mock import patch
from largest_number import main

class TestLargestNumber(unittest.TestCase):

    @patch('builtins.input', lambda: '10 9 12 15')
    def test_largest_number_1(self):
        self.assertEqual(main(), 1512109)

    @patch('builtins.input', lambda: '90 15 30 45 95 105')
    def test_largest_number_2(self):
        self.assertEqual(main(), 1059590453015)


if __name__ == "__main__":
    unittest.main()
