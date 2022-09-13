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

    @property
    def size(self):
        """getter function to get the atrr"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter function to set the attr"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        size.__size = value
