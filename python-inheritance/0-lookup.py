#!/usr/bin/python3
"""This module returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    list_attribute = dir(obj)
    return list_attribute
