#!/usr/bin/python3
"""
module contains a function that
inserts a line of text to a file
arter each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """function that searches and adds"""
    with open(filename, "r", encoding="utf-8") as fp:
        r = fp.readlines()
    new_data = []
    for i in range(len(r)):
        new_data.append(r[i])
        if search_string in r[i]:
            new_data.append(new_string * 2)

    with open(filename, "w", encoding="utf-8") as fp:
        fp.writelines(new_data)
