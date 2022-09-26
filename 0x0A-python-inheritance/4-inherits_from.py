#!/usr/bin/python3
"""
ciintains one function inherits from
"""


def inherits_from(obj, a_class):
    """
    function that chechs if a class is
    an instance of a class directly or
    indirectly
    """
    return isinstance(obj, a_class) and type(obj) != a_class
