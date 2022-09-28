#!/usr/bin/python3
"""
contains a function that
returns the dictionary description
with simple data structures (list, dictionary,
sting, integer and boolean) for JSON
serialization of an object
"""


def class_to_json(obj):
    """returns the dict description that is al the atrr
    in an object"""
    return obj.__dict__
