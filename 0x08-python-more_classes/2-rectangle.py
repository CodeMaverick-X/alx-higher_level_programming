#!/usr/bin/python3
"""
a module that contains a class that defines a
rectangle
"""


class Rectangle:
    """
    kinda empty
    """

    def __init__(self, width=0, height=0):
        """instantiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width field"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calcs the are no test cases"""
        return self.__width * self.__height

    def perimeter(self):
        """calcs the perimeter no test cases"""
        if self.__weight == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__weight
