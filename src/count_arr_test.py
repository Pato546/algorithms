#!/usr/bin/env python3

from count_arr import count_arr
import unittest


class TestCount(unittest.TestCase):

    def test_count(self):
        self.assertEqual(count_arr([1,2,3]), 3)
        self.assertEqual(count_arr([2]), 1)

    def test_count_empty(self):
        self.assertEqual(count_arr([]), 0)

unittest.main()
