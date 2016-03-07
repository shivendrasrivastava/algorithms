__author__ = "Shiven"

import unittest
from unittest.mock import patch
from fibonacci import fibonacci
import time

class TestFibonacci(unittest.TestCase):

    @patch('builtins.input', lambda: 10)
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(), 55)

    @patch('builtins.input', lambda: 90)
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(), 2880067194370816120)

    @patch('builtins.input', lambda: 100)
    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(), 354224848179261915075)

    @patch('builtins.input', lambda: 354)
    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(), 42868634127888159424995674777973502051063092312442448224088410550266867672)

    @patch('builtins.input', lambda: 20)
    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(), 6765)

    @patch('builtins.input', lambda: 60)
    def test_fibonacci_6(self):
        self.assertEqual(fibonacci(), 1548008755920)

    @patch('builtins.input', lambda: 70)
    def test_fibonacci_7(self):
        self.assertEqual(fibonacci(), 190392490709135)

    @patch('builtins.input', lambda: 88)
    def test_fibonacci_8(self):
        self.assertEqual(fibonacci(), 1100087778366101931)

    @patch('builtins.input', lambda: 71)
    def test_fibonacci_9(self):
        self.assertEqual(fibonacci(), 308061521170129)

if __name__ == "__main__":
    unittest.main()
