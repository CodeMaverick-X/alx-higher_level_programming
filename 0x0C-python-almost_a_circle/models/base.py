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
        """convert list of dictionary to json str"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            e_data = json.dumps(list_dictionaries)
            return e_data

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to file"""
        list_dict = []
        for i in list_objs:
            list_dict.append(i.to_dictionary())

        e_data = Base.to_json_string(list_dict)

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(e_data)


