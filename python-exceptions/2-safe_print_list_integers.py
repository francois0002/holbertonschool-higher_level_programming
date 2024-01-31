#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    count = 0
    try:
        while index < x:
            if isinstance(my_list[index], int):
                print("{}".format(my_list[index]), end="")
                index += 1
                count += 1
            else:
                index += 1

    except IndexError:
        pass
    except:
        pass
    print()
    return count
