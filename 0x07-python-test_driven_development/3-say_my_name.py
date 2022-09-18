#!/usr/bin/python3
"""
Module that prints my nae is
firstname lastname, where firstname is required
and last name is not, both parameters must be str
"""


def say_my_name(first_name, last_name=""):
    """
    function say_my_name prints the sentecce
    my name is firstname lastname where bothe names must
    be str and firstname is required
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    message = "My name is {} {}"

    print(message.format(first_name, last_name))
