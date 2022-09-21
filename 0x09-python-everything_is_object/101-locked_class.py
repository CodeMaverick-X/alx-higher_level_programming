#!/usr/bin/python3
class LockedClass:

    __slots__ = ['first_name', 'f_name']

    def __init__(self, first_name=''):
        self.f_name = first_name


    @property
    def first_name(self):
        return self.f_name

    @first_name.setter
    def first_name(self, value):
        self.f_name = value


