#!/usr/bin/python3
"""
writing to a file
"""


def write_file(filename="", text=""):
    """writes to a file <filename>"""

    with open(filename, "w", encoding="utf-8") as fp:
        w = fp.write(text)
        return w
