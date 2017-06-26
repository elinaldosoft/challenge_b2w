#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections
from exceptions import InValidTriangle, NoTriangleValid

__author__ = '@elinaldosoft'


def prepare_matrix(matrix):
    order, matrix_sorted, rows = {}, [], []

    for row in matrix:
        key = len(row)
        rows.append(key)

        if key in order.keys() or not all(isinstance(item, int) for item in row):
            raise InValidTriangle('It is not triangle valid', '001')
        order[key] = row

    if not [x for x in range(1, len(matrix) + 1)] == sorted(rows):
        raise NoTriangleValid('Not a triangle with equal sides', '002')

    for key, values in collections.OrderedDict(sorted(order.items())).items():
        matrix_sorted.append(values)

    return matrix_sorted


def get_values(matrix):
        matrix = prepare_matrix(matrix)
        current_number, values_selections_triangle = 0, []

        for row in matrix:
            count = 1
            while True:

                if len(row) == 1:
                    current_number = row[0]
                    values_selections_triangle.append(current_number)
                    break

                current_number_inc = current_number + count
                current_number_dec = current_number - count

                if max(row) > current_number and current_number_inc in row:
                    values_selections_triangle.append(current_number_inc)
                    current_number = current_number_inc
                    break
                elif max(row) < current_number and current_number_dec in row:
                    values_selections_triangle.append(current_number_dec)
                    current_number = current_number_dec
                    break

                if count == max(row):
                    break
                count += 1

        return values_selections_triangle


def summed(values):
    return sum(values)
