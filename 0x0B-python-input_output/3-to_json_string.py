#!/usr/bin/python3
"""
module that contains a function
to_json_string that returns the
json representation of an ogject
(string)
"""

import json


def to_json_string(my_obj):
    """converts obj to to json representation"""
    return json.dumps(my_obj)
