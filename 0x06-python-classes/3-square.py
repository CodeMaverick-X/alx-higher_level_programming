#!/usr/bin/python3
"""this script defines a square based on the last file"""


class Square:
    """definition of a class named square that calculates
    the area of a square"""

    def __init__(self, size=0):
        """initialises the size obj attr
        to size that was pased in
        private instance attribute: size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of a square
        Public instance method: def area(self):"""

        return self.__size * self.__size
