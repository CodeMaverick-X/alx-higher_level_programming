#!/usr/bin/python3
"""
this module contains the function matrix_divide which
is used to devide a matrix
by a number - basic
"""


def matrix_divided(matrix, div):
    """
    function matrix_divided is used to divide a matix(list of list)
    by an int or float
    """
    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
        for lst1 in lst:
            if not isinstance(lst1, int) and not isinstance(lst1, float):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    length = len(matrix[0])

    for lst in matrix:
        if len(lst) != length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrx = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrx
