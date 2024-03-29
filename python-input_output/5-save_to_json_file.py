#!/usr/bin/python3
"""Module that writes an Object to a text file,
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    json_content = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_content)
