__author__="Shiven"

import unittest
from unittest.mock import patch
from fibonacci_last_digit import main

class TestFibonacciLastDigit(unittest.TestCase):

    @patch('builtins.input', lambda: 10)
    def test_fibonacci_last_digit_1(self):
        self.assertEqual(main(), 5)

    @patch('builtins.input', lambda: 90)
    def test_fibonacci_2(self):
        self.assertEqual(main(), 0)

    @patch('builtins.input', lambda: 100)
    def test_fibonacci_3(self):
        self.assertEqual(main(), 5)

    @patch('builtins.input', lambda: 354)
    def test_fibonacci_4(self):
        self.assertEqual(main(), 2)

    @patch('builtins.input', lambda: 20)
    def test_fibonacci_5(self):
        self.assertEqual(main(), 5)

    @patch('builtins.input', lambda: 60)
    def test_fibonacci_6(self):
        self.assertEqual(main(), 0)

    @patch('builtins.input', lambda: 70)
    def test_fibonacci_7(self):
        self.assertEqual(main(), 5)

    @patch('builtins.input', lambda: 88)
    def test_fibonacci_8(self):
        self.assertEqual(main(), 1)

    @patch('builtins.input', lambda: 71)
    def test_fibonacci_9(self):
        self.assertEqual(main(), 9)

    @patch('builtins.input', lambda: 200)
    def test_fibonacci_10(self):
        self.assertEqual(main(), 5)

    @patch('builtins.input', lambda: 354)
    def test_fibonacci_11(self):
        self.assertEqual(main(), 2)

    @patch('builtins.input', lambda: 566)
    def test_fibonacci_12(self):
        self.assertEqual(main(), 3)

    @patch('builtins.input', lambda: 5668)
    def test_fibonacci_13(self):
        self.assertEqual(main(), 1)

    @patch('builtins.input', lambda: 8786)
    def test_fibonacci_14(self):
        self.assertEqual(main(), 3)


if __name__ == "__main__":
    unittest.main()
