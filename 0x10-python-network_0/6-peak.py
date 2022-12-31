#!/usr/bin/python3
"""
function that finds peak in a list
"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    i = len(list_of_integers)

    if i < 1 or list_of_integers is None:
        return None

    if i == 1:
        return list_of_integers

    new = max(list_of_integers)
    return new
