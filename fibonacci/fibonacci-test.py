__author__ = "Shiven"

import unittest
from unittest.mock import patch
from fibonacci import fibonacci
import time

class TestFibonacci(unittest.TestCase):

    @patch('builtins.input', lambda: 10)
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(), 55)

    @patch('builtins.input', lambda: 100)
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(), 354224848179261915075)

    @patch('builtins.input', lambda: 354)
    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(), 42868634127888159424995674777973502051063092312442448224088410550266867672)

if __name__ == "__main__":
    unittest.main()
