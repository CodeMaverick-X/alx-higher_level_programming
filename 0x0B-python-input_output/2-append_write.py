#!/usr/bin/python3
"""
appending to a file
"""


def append_write(filename="", text=""):
    """appends to a file <filename>"""

    with open(filename, "a", encoding="utf-8") as fp:
        w = fp.write(text)
        return w
