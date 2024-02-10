#!/usr/bin/python3
"""This module add 2 numbers

This module make a operation an compute two numbers,
these numbers can be integers or floats.

"""


def add_integer(a, b=98):
    """Add 2 integers
    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.

        Return : (int) the result of the addition
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) is True:
        int(a)
    if isinstance(b, float) is True:
        int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

