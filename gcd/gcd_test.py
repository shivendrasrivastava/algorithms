#Uses python3
__author__ = "Shiven"

import unittest
from gcd import gcd
from unittest.mock import patch

class TestGCD(unittest.TestCase):

    @patch('builtins.input', lambda: '108 30')
    def test_gcd_1(self):
        self.assertEqual(gcd(), 6)

    @patch('builtins.input', lambda: '28851538 1183019')
    def test_gcd_2(self):
        self.assertEqual(gcd(), 17657)

    @patch('builtins.input', lambda: '163231 152057')
    def test_gcd_3(self):
        self.assertEqual(gcd(), 151)

if __name__ == "__main__":
    unittest.main()
