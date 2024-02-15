#!/usr/bin/python3
""" Module that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, "r") as file:
        content = file.read()
        print("{}".format(content), end="")
