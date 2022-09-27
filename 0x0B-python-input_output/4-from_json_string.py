#!/usr/bin/python3
"""
module contains function that converts
json represented obj back to py obj
json string to py obj
"""


import json


def from_json_string(my_str):
    return json.loads(my_str)
