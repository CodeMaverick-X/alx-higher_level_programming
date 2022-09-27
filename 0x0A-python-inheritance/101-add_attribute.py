#!/usr/bin/python3
"""
tries to modif a parent class
if possible
"""


def add_attribute(obj, attr, value):
    """adds new attr"""

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
