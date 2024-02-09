#!/usr/bin/python3
"""This module creates an empty class named Square"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) is True:
        int(a)
    if isinstance(b, float) is True:
        int(b)
    return a + b


