#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    result = 0
    nbr_args = len(argv)

    for x in range(1, nbr_args):
        result = result + int(argv[x])
    print(result)
