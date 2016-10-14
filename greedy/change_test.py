#Uses python3
__author__ = "Shiven"

import unittest
from unittest.mock import patch
from change import main

class TestChangeGreedy(unittest.TestCase):

    @patch('builtins.input', lambda: 28)
    def test_change_greedy_1(self):
        self.assertEqual(main(), 6)

    @patch('builtins.input', lambda: 27)
    def test_change_greedy_2(self):
        self.assertEqual(main(), 5)

    @patch('builtins.input', lambda: 999)
    def test_change_greedy_3(self):
        self.assertEqual(main(), 104)

    @patch('builtins.input', lambda: 272)
    def test_change_greedy_4(self):
        self.assertEqual(main(), 29)

    @patch('builtins.input', lambda: 873)
    def test_change_greedy_5(self):
        self.assertEqual(main(), 90)

    @patch('builtins.input', lambda: 1)
    def test_change_greedy_6(self):
        self.assertEqual(main(), 1)

    @patch('builtins.input', lambda: 333)
    def test_change_greedy_7(self):
        self.assertEqual(main(), 36)

    @patch('builtins.input', lambda: 2)
    def test_change_greedy_8(self):
        self.assertEqual(main(), 2)

    @patch('builtins.input', lambda:5)
    def test_change_greedy_9(self):
        self.assertEqual(main(), 1)


if __name__ == "__main__":
    unittest.main()
