#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from binary_search import binary_search
import unittest


class TestBinarySearch(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 1), 0)

    def test_empty(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 7), -1)

    def __str__(self):
        return 'TestBinarySearch'

unittest.main()
