#!/usr/bin/python3
"""
rectangle  module
"""

from models.base import Base


class Rectangle(Base):
    """racctangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instance constructor
        Args:
            - width: (required arg) width of the rectangle
            - height: (required arg) heighgt of the rectangle
            - x: offset on the x plane
            - y: offset on the y plane
            - id: instance id set by base class
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            - value: width value, must be an integer and must
            be greater than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            - value: height value, must be an integer and must
            be greater than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y getter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """displays the triangle in stdout with #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """string print"""
        message = "[Rectangle] ({}) {}/{} - {}/{}"
        return message.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the intsnce attrr"""
        attr = ["id", "width", "height", "x", "y"]

        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for i in kwargs:
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """returns the rectangle dict"""

        dic = {"id": self.id, "width": self.width,
               "height": self.height, "x": self.x, "y": self.y}

        return dic
