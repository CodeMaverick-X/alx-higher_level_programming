#!/usr/bin/python3
"""
module contains a function
is kind of class
"""


def is_kind_of_class(obj, a_class):
    """
    func that compares an obj to
    a class for approximate equality
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
