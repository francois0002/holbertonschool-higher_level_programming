#!/usr/bin/python3

import sys

if __name__ == "__main__":

    x = 1

    if len(sys.argv) == 1:
        print("{} arguments".format(len(sys.argv) - 1))

    elif len(sys.argv) == 2:
        print("{} argument".format(len(sys.argv) - 1))
        print("{}: {}".format(x, sys.argv[x]))

    else:

        print("{} arguments".format(len(sys.argv) - 1))
        while x < len(sys.argv):
            print("{}: {}".format(x, sys.argv[x]))
            x = x + 1
