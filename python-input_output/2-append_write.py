#!/usr/bin/python3
""" Module that appends a string at the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file
        and returns the number of characters added"""
    with open(filename, "a") as file:
        file.write(text)
        return len(text)
