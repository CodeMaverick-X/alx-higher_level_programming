#!/usr/bin/python3
"""
module to get a list of list
containting pascals triangle value
"""


def fact(n):
    """find the factorail using recursion"""
    if n == 1 or n == 0:
        return 1

    ans = n * fact(n - 1)
    return ans


def pascal_triangle(n):
    """
    pascal triangle using the formular
    iCj where c means combination
    args:
        - n: value to find pascal t for
    Return: list of list
    """
    base = []

    for i in range(0, n):
        sub = []
        for j in range(0, i + 1):
            sub.append(fact(i)//(fact(i - j) * fact(j)))
        base.append(sub)

    return base
