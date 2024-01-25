#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    nbr_args = len(sys.argv)
    if nbr_args == 1:
        print("{} arguments.".format(nbr_args - 1))
    elif nbr_args == 2:
        print("{} argument:".format(nbr_args - 1))
    else:
        print("{} arguments:".format(nbr_args - 1))
    for i in range(1, nbr_args):
        print("{}: {}".format(i, sys.argv[i]))
