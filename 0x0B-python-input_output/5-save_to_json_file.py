#!/usr/bin/python3
"""
module contains a function that
writes an obj to a text file,
using json representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, "w", encoding="utf-8") as fp:
        e_data = json.dumps(my_obj)
        w = fp.write(e_data)
