#!/usr/bin/python3
def safe_print_integer(value):
    try:
        number = int(value)
        print("{:d}".format(number))

    except:
        return False

    else:
        return True
