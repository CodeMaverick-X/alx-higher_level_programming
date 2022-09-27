#!/usr/bin/python3
"""
module that contains a function that
adds all arguments to a python list
and then saves them to a file
"""


import json
from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"
py_list = []

if path.exists(file_name) and path.getsize(file_name) > 0:
    py_list = load_from_json_file(file_name)

for i in argv[1:]:
    py_list.append(i)

save_to_json_file(py_list, file_name)
