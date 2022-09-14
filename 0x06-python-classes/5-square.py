#!/usr/bin/python3
"""this script defines a square based on the last file"""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """initialises the size obj attr
        to size that was pased in
        private instance attribute: size"""

        self.size = size

    def area(self):
        """returning the area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """print the square #"""

        if self.__size != 0:
            for i in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print()
        elif self.__size == 0:
            print()

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
        self.__size = value
