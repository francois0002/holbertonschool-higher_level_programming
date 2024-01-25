#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    x = 1

    if len(argv) == 1:
        print("0 arguments")

    elif len(argv) == 2:
        print("1 argument")
        print("{}: {}".format(x, argv[x]))

    else:

        print("{} arguments".format(len(argv) - 1))
        while x < len(argv):
            print("{}: {}".format(x, argv[x]))
            x = x + 1
