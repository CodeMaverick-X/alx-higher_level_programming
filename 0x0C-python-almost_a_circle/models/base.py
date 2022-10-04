#!/usr/bin/python3
"""
module base
defines a base class for other classes in this project
"""

import csv
import json
from os import path


class Base:
    """
    base class
     private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        instance contructor
        Args:
            - id: id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list of dictionary to json str

        Args:
            - list_dictionary: list of dictionary

        Returns: JSON representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            e_data = json.dumps(list_dictionaries)
            return e_data

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json string representation of list_objs to file

        Args:
            - list_objs: a list of objects or instances

        Description: get the dictionary representation of the objects
        with the instance function and store all the instances in a list
        and convert the list to a json strin and store it in a file
        """
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
        Args:
            - json_string: json string to be converted to python list
        Returns: the list of the JSON string representation
        """
        if json_string is None:
            return []
        else:
            d_data = json.loads(json_string)
            return d_data

    @classmethod
    def create(cls, **dictionary):
        """
        class method
        returns an instance with all attributes already set
        Args:
            - dictionary: kwargs of dictionary
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
        class method
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves to csv file
        Args:
            - list_objs: list of objects
        """
        list_dict = []
        if list_objs is None or list_objs == []:
            e_data = "[]"
        else:
            for i in list_objs:
                list_dict.append(i.to_dictionary())

        if cls.__name__ == "Rectangle":
            dict_f = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            dict_f = ["id", "size", "x", "y"]

        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as fp:
            writer = csv.DictWriter(fp, fieldnames = dict_f)
            writer.writeheader()
            writer.writerows(list_dict)


    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.
        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        l = []
        if path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        l.append(i)
        return l
