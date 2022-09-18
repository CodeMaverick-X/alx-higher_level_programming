#!/usr/bin/python3
"""
Module print_square
prints a square with # of area of size
"""


def print_square(size):
    """
    print a square wher size is used
    as the length and width
    """

    if size is None or not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
