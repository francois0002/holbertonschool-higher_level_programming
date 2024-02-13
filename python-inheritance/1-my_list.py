#!/usr/bin/python3
"""print the list named List sorted"""


class MyList(list):
    """print the list named List sorted"""
    def print_sorted(self):
        """print the list named List sorted"""
        if MyList is not None:
            sorted_list = sorted(self)
            print("{}".format(sorted_list))
        else:
            return None
