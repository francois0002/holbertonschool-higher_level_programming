#!/usr/bin/python3

def no_c(my_string):
    new_list = []
    for letter in my_string:
        if letter != "c" and letter != "C":
            new_list.append(letter)

    new_string = ''.join(new_list)

    return new_string

    """
    for index in range(len(new_list)):
        if new_list[index] == "c" or new_list[index] == "C":
            new_list[index] == []
        else:
            pass
    """
