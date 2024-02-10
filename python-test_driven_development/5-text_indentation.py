#!/usr/bin/python3
"""This modulethat prints a text with 2 new lines after
   each of these characters: "." "?" and ":"

"""


def text_indentation(text):
    """
        prints a text with 2 new lines
        Args:
        test (str) : string to indente
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text):
        if text[index] in [':', '.', '?']:
            print(text[index])
            print()
            a += 1
        else:
            print(text[index], end='')
        a += 1
