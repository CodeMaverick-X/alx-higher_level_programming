#!/usr/bin/python3
"""
student module
contains student class
"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of student"""
        new = {}

        if attrs is None:
            return self.__dict__
        else:
            for l in attrs:
                if l in self.__dict__:
                    new[l] = self.__dict__[l]

            return new
