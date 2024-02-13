#!/usr/bin/python3
""" Modules that contains a class BaseGeometry
Class Rectangle inherit from BaseGeometry"""


class BaseGeometry:
    """raises an Exception with the message area() is not implemented"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than O".format(name))


class Rectangle(BaseGeometry):
    """Class that inherit from BaseGeometry"""
    def __init__(self, width, height):
        """init the width of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
