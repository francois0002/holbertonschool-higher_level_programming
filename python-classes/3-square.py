#!/usr/bin/python3
"""This module initialize a class named Square"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Compute and return the square area"""
        return self.__size * self.__size
