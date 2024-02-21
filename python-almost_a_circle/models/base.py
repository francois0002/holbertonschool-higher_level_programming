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

    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_dict = []
        if list_objs is None:
            list_objs = []

        for items in list_objs:
            list_dict.append(items.to_dictionary())

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
         """ Returns an instance with all attributes already set:"""
         if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
