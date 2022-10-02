#!/usr/bin/python3
"""
module base
"""


import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instance contructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            e_data = json.dumps(list_dictionaries)
            return e_data
