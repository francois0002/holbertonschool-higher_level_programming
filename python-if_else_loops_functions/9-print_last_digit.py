#!/usr/bin/python3

def print_last_digit(number):

    if number >= 0:
        print(number % 10, end="")
        last_digit = number % 10
        return last_digit
    else:
        number = number * -1
        print(number % 10, end="")
        last_digit = number % 10
        return last_digit
