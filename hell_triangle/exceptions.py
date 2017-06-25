#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = '@elinaldosoft'


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InValidTriangle(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
