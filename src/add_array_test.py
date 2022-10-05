#!/usr/bin/env python3

from add_array import sum_arr
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum_arr([2,4,6]), 12)
        self.assertEqual(sum_arr([1,9,10,45,89,90]), 244)
        self.assertEqual(sum_arr([2]), 2)

    def test_empty_arr(self):
        self.assertEqual(sum_arr([]), 0)

unittest.main()
