#!/usr/bin/python3
"""Module that adds all arguments to a Python list, and then save them to a file”"""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file



def args_in_file(filename):
    """Adds all arguments to a Python list, and then save them to a file”"""
    arguments_list = sys.argv[1:]
    list_json = load_from_json_file(arguments_list)
    save_to_json_file(list_json)
