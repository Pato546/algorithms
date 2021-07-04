#!/usr/bin/env python3
from selection_sort import selection_sort
import unittest

class SelectionSort(unittest.TestCase):

    def test_array_ascending(self):
        self.assertEqual(selection_sort([1,5,2,3,4,8]), [1,2,3,4,5,8])

    def test_array_descending(self):
        self.assertEqual(selection_sort([1,5,2,3,4,8], reverse=True), [8,5,4,3,2,1])

    def test_array_empty(self):
        self.assertEqual(selection_sort([]), 'cannot sort an empty list')



unittest.main()
