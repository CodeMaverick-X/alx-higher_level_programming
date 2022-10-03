#!/usr/bin/python3
"""
module base
"""


import json
from os import path


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
        if list_objs is None or list_objs == []:
            e_data = "[]"
        else:
            for i in list_objs:
                list_dict.append(i.to_dictionary())

            e_data = Base.to_json_string(list_dict)

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(e_data)

    @staticmethod
    def from_json_string(json_string):
        """
        from json to string
        that returns the list of the JSON string representation
        """
        if json_string is None:
            return []
        else:
            d_data = json.loads(json_string)
            return d_data

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances that where loaded from
        a file, hence the name load from file duhh
        """

        filename = cls.__name__ + ".json"
        if path.exists(filename) and path.getsize(filename) > 0:
            instance = []
            with open(filename, encoding="utf-8") as fp:
                e_data = fp.read()
                d_data = Base.from_json_string(e_data)

                for i in d_data:
                    sub = cls.create(**i)
                    instance.append(sub)
            return instance

        else:
            return []
