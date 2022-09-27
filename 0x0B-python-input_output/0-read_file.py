#!/usr/bin/python3
"""
mod to read a text file and print to stdout
"""


def read_file(filename=""):
    """opens <filename> and prints to stdout"""

    with open(filename, encoding="utf-8") as fp:
        data = fp.read()
        print(data)
