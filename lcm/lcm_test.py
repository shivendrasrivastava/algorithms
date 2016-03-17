#Uses python3

import unittest
from unittest.mock import patch
from lcm import lcm

class TestLCM(unittest.TestCase):

    @patch('builtins.input', lambda: '108 30')
    def test_lcm_1(self):
        self.assertEqual(lcm(), 540)

    @patch('builtins.input', lambda: '2800 300')
    def test_lcm_2(self):
        self.assertEqual(lcm(), 8400)

    @patch('builtins.input', lambda: '600 389')
    def test_lcm_3(self):
        self.assertEqual(lcm(), 233400)

    @patch('builtins.input', lambda: '226553150 1023473145')
    def test_lcm_4(self):
        self.assertEqual(lcm(), 46374212988031350)

if __name__ == '__main__':
    unittest.main()
