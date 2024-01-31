#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))

    except (IndexError, ValueError):
        return False

    else:
        return True
