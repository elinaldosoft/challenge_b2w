#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from trianglehell import get_values, summed
import fire

__author__ = '@elinaldosoft'


def matrix(values):
    values_selected = get_values(values)
    result = summed(values_selected)
    message = "Numbers selected {} = {}".format(" + ".join([str(x) for x in values_selected]), result)
    return message

if __name__ == '__main__':
    fire.Fire()
