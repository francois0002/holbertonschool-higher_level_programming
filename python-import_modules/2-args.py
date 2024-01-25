#!/usr/bin/python3

import sys

if __name__ == "__main__":

    x = 1

    if len(sys.argv) == 1:
        print("{:d} arguments".format(len(sys.argv) - 1))

    elif len(sys.argv) == 2:
        print("{:d} argument".format(len(sys.argv) - 1))
        print("{:d}: {}".format(x, sys.argv[x]))

    else:

        print("{} arguments".format(len(sys.argv) - 1))
        while x < len(sys.argv):
            print("{:d}: {}".format(x, sys.argv[x]))
            x = x + 1
