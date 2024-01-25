#!/usr/bin/python3


if __name__ == "__main__":

    from sys import argv

    x = 1

    if len(argv) == 1:
        print("0 arguments")

    elif len(argv) == 2:
        print("1 argument")
        print("{}: {}".format(x, argv[x]))

    else:

        print("{} arguments".format(len(argv) - 1))
        for x in range(1, len(argv)):
            print("{}: {}".format(x, argv[x]))

