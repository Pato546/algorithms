#!/usr/bin/env python3

from find_min_max import min_, max_
import unittest

class Minimum_Maximum(unittest.TestCase):

    def test_min(self):
        self.assertEqual(min_([1,2,3,0,4,6,8]),3)
        self.assertEqual(min_([2,3,4,5,6,7,8]), 0)
    
    def test_max(self):
        self.assertEqual(max_([1,2,3,4,5,6,7]), 6)

unittest.main()

    
