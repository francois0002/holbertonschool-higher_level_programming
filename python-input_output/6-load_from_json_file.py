#!/usr/bin/python3
"""This module creates an empty class named Rectangle"""


class Rectangle:
    """Define a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle
        """
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0 or height < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0 or height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ get & set the width of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ get & set the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def perimeter(self):
        """ Compute and return the rectangle area"""
        if (self.__width + self.__height) * 2 == 0:
            return 0
        return (self.__width + self.__height) * 2

    def area(self):
        """ Compute and return the rectangle perimeter"""
        return self.__width * self.__height

    def __str__(self):
        """ return a rectangle with the character #"""
        rectangle_string = ""
        if self.width == 0 or self.height == 0:
            return (rectangle_string)
        for row in range(self.height):
            for column in range(self.width):
                rectangle_string += "#"
            rectangle_string += "\n"
        rectangle_string = rectangle_string[:-1]
        return (rectangle_string)

    def __repr__(self):
        """returns string representation of rectangle"""
        rectangle_string = "Rectangle(%s, %s)" % (self.width, self.height)
        return (rectangle_string)

    def __del__(self):
        """Delete an instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
