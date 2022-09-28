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

    def to_json(self):
        """retrieves a dict representation of student"""
        return self.__dict__
