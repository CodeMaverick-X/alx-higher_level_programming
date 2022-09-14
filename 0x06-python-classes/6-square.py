#!/usr/bin/python3
"""thjis is script that defines a class square that
is based on the file 5-square.py"""


class Square:
    """class square defines a square that describes an object for
    square instances with a private size attr"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation of the o fthe object with private instance
        size which is 0 by default"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """getter function to return the size attr"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function to set the size attr"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter function for position attr"""
        return self.__position

    @position.setter
    def position(self, val):
        """settet methjod for position atrr"""
        if not isinstance(val, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(val[0], int) or not isinstance(val[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        elif self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
