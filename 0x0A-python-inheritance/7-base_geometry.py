#!/usr/bin/python3
"""
module for geometry
"""


class BaseGeometry:
    """
    has to do with some geometry
    """

    def area(self):
        """area is not yet implimented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0")
