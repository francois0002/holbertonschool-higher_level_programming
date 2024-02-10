#!/usr/bin/python3
"""This module print a square with the character #

example :

####
####
####
####

"""


def print_square(size):
    """
        Print square using #
        Args:
        size (int) : Size of Square
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print('#', end='')

            if j % size == 0 and j > 0:
                print()
