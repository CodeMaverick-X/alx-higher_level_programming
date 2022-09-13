#!/usr/bin/python3
"""thios file containts a script that defines a square
based on 1-square.py"""


class Square:
    """class square that defines a square
    Private instance attribute: size
    instantiotion with optional size"""

    def __init__(self, size=0):
        """instantiotion of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
