#!/usr/bin/python3
"""
module 100-my-int
"""


class MyInt(int):
    """
    my iont is a rebel class that inherits from
    int. my in has == and != inverted
    """

    def __eq__(self, other):
        """invert eguality"""

        return super().__ne__(other)

    def __ne__(self, other):
        """ inverts inequaity"""

        return super().__eq__(other)
