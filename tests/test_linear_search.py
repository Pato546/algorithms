#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from linear_search import linear_search
import unittest


class TestLinearSearch(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(linear_search([2, 4, 6, 7, 8], 8), 4)
        self.assertEqual(linear_search(['Patrick', 'Ababio', 'Twum'], 'Patrick'), 0)
        self.assertEqual(linear_search([3, 6, 9], 12), -1)




unittest.main()
