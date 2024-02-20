#!/usr/bin/python3
""" class that named Base """


import json


class Base:
    """ Base of all others class in the project. Goal : manage id attribute
    in all future classes and to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        else:
            str_json = json.dumps(list_dictionaries)
            return str_json
