#!/usr/bin/python3
"""
module 0-add_ntigers: module contains one functioncalled add_intiges
"""


def add_integer(a, b=98):
    """
    function that recieves two intigers or floats and returns
    the adition of the two values
    """
    if (not isinstance(a, int) and not isinstance(a, float)) or a is None:
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)
    return a + b
