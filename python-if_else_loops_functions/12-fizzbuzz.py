#!/usr/bin/python3

def multiple_3(x):
    if x % 3 == 0:
        return True


def multiple_5(x):
    if x % 5 == 0:
        return True


def fizzbuzz():
    for x in range(1, 101):
        if multiple_3(x) is True and multiple_5(x) is True:
            x = str(x)
            x = "FizzBuzz"
            print(x, end=" ")

        elif multiple_3(x) is True:
            x = str(x)
            x = "Fizz"
            print(x, end=" ")

        elif multiple_5(x) is True:
            x = str(x)
            x = "Buzz"
            print(x, end=" ")

        else:
            print(x, end=" ")
