#!/usr/bin/python3
"""This module print the first name and the last name

This module print with this format :
My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """Add 2 integers
    Args:
        first_name (:obj:`string`): The first name.
       last_name (:obj:`str): The last_name.

        Return : none
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
