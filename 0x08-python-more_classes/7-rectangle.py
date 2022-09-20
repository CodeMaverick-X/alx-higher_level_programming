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
        Rectangle.number_of_instances += 1

    number_of_instances = 0
    print_symbol = '#'

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """printabe string of the class"""
        if self.__width == 0 or self.__height == 0:
            return ""
        str_ver = ""
        for h in range(self.__height):
            for w in range(self.__width):
                str_ver += str(self.print_symbol)
            if h != (self.__height - 1):
                str_ver += "\n"
        return str_ver

    def __repr__(self):
        """_repr_"""
        return "Rectangle(" + str(self.__width) +\
            ", " + str(self.__height) + ")"

    def __del__(self):
        """deleting"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
