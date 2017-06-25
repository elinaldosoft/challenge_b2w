#!/usr/bin/python
# -*- coding: utf-8 -*-
from hell_triangle.trianglehell import get_values, summed

__author__ = '@elinaldosoft'


def run():
    triangle = [
        [6],
        [3, 5],
        [9, 7, 1],
        [4, 6, 8, 4]

    ]

    values_selected = get_values(triangle)
    result_end = summed(values_selected)
    print("Numbers selected {} = {}".format(values_selected, result_end))


if __name__ == "__main__":
    run()
