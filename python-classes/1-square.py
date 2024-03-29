#!/usr/bin/python3
"""This module initialize a class named Square"""


class Square:
    """Define a square
    Attributes:
    attr1 (size): size of square"""
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
