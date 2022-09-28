#!/usr/bin/python3
"""
student module
contains student class

@class: Student
"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Description: instantiation

        @first_name: students firt name
        @last_name: students last name
        @age: students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Discription: retrieves a dict representation
        of student

        @attrs: list of atrributes
        Return: dictionary
        """
        if attrs is None:
            return self.__dict__
        else:
            new = {}
            for l in attrs:
                if l in self.__dict__:
                    new[l] = self.__dict__[l]

            return new
