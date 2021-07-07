#!/usr/bin/env python3
from quick_sort import quick_sort
import unittest


class TestQuickSort(unittest.TestCase):
    
    def test_arr(self):
        self.assertEqual(quick_sort([2, 5, 3, 6]), [2, 3, 5, 6])
        self.assertEqual(quick_sort([2, 9, 3, 1, 8, 7]), [1, 2, 3, 7, 8, 9]) 

    def test_empty_arr(self):
        self.assertEqual(quick_sort([]), [])

    def test_duplicate_arr(self):
        self.assertEqual(quick_sort([9, 2, 8, 4, 2, 3]), [2, 2, 3, 4, 8, 9])

unittest.main()
