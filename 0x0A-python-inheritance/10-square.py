#!/usr/bin/python3
"""
module 10-square
inherits from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class square that defines a square
    """

    def __init__(self, size):
        """instantiation"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str print"""
        return super().__str__()

    def area(self):
        return self.__size ** 2
