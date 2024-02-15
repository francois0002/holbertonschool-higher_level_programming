#!/usr/bin/python3
"""Module that write a function that creates
 an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file"""

    with open(filename, "r") as file:
        json_conversion = json.load(file)

    return json_conversion
