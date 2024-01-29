#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list == []:
        return None

    for index in range(len(my_list)):
        if index == 0:
            max_number = my_list[index]
        else:
            if my_list[index] > max_number:
                max_number = my_list[index]
            else:
                continue

    return max_number
