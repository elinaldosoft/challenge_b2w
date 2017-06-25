#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from hell_triangle.trianglehell import get_values, prepare_matrix, summed
from hell_triangle.exceptions import InValidTriangle

__author__ = '@elinaldosoft'


class TestHellTriangle(unittest.TestCase):

    def test_values_triangle_hell(self):
        self.assertEqual(get_values([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]), [6, 5, 7, 8])
        self.assertEqual(get_values([[6], [3, 5], [9, 8, 1], [4, 6, 9, 4]]), [6, 5, 8, 9])
        self.assertEqual(get_values([[6], [5, 8], [10, 12, 15], [5, 4, 3, 2]]), [6, 8, 10, 5])
        self.assertEqual(get_values([[1], [2, 3], [10, 15, 20], [30, 4, 8, 9], [10, 12, 15, 17, 13]]), [1, 2, 10, 30, 17])
        self.assertEqual(get_values([[-1], [0, 1], [-2, -3, -4], [5, 2, 3, 6]]), [-1, 0, -2, 2])
        self.assertEqual(get_values([[1], [0, 2]]), [1, 2])

        with self.assertRaises(InValidTriangle) as cm:
            get_values([[6], [9, 7, 1], [9, 7, 1], [4, 6, 8, 4]])
        self.assertEqual(
            "('It is not triangle valid', '001')",
            str(cm.exception)
        )

    def test_prepare_matrix(self):
        self.assertEqual([[1], [2, 1], [9, 7, 1]], prepare_matrix([[9, 7, 1], [2, 1], [1]]))

    def test_summed_values_found_triangle(self):
        values = get_values([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]])
        self.assertEqual(summed(values), 26)
