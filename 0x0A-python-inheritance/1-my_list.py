#!/usr/bin/python3
"""
mod: contains class mylist
"""


class MyList(list):
    """
    class that inherits from list that acts as like
    an extension...giberish
    """

    def print_sorted(self):
        """
        prints a sorted list in ascending order
        """
        print(sorted(self))
