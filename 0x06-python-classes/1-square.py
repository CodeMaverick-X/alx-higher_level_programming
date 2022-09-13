#!/usr/bin/python3
"""this class creates a class named square and initialises it"""
class Square:
    """square class based on 0-sqaure.py
    Instantiation with size (no type/value verification).
    private instance attribute: size"""

    def __init__(self, size):
        """initialises the size attr"""
        self.__size = size

