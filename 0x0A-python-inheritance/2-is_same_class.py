#!/usr/bin/python3
"""
mod: contains func that compares types
"""


def is_same_class(obj, a_class):
    """
    function that compares types
    """
    if type(obj) is a_class:
        return True
    else:
        return False
