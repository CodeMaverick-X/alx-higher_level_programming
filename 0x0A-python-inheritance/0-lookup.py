#!/usr/bin/python3
"""
module: 0-lookup contains a function called lookup
that returns the list of available attr and methods
of an object.
"""
def lookup(obj):
    """
    arg: obj which is an object
    return list of all attr and methods
    """
    return list(dir(obj))
