#!/usr/bin/python3
"""This module initialize a class named Square"""

class Square:
    """Define a square"""
    def __init__(self, size=0, ):
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

    def my_print(self):
        """ Print a square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """ get & set the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
