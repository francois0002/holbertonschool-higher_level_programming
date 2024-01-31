#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    list_keys = list(new_dictionary.keys())

    for index in list_keys:
        new_dictionary[index] = new_dictionary[index] * 2

    return (new_dictionary)
