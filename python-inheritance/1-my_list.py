#!/usr/bin/python3
""" implement sorted list"""


class MyList(list):
    """Implements sorted list for class Mylist."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
