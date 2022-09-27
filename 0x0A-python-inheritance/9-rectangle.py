#!/usr/bin/python3
"""
module 8-rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle that iomports from base geaometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """string print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area of a rectangle h * w"""
        return self.__width * self.__height
