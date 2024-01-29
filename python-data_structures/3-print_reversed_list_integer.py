#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for value in my_list:
        print("{}".format(value))
    my_list.reverse()
