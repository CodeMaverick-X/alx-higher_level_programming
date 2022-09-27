#!/usr/bin/python3
"""
module contains a function that create
an obj from a json file
"""


import json


def load_from_json_file(filename):
    """function that creates obj from a json file"""
    with open(filename, encoding="utf-8") as fp:
        e_data = fp.read()
        d_data = json.loads(e_data)
        return d_data
