#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        
        new = matrix.copy()
        for i in range(0, len(new)):
            for j in range(len(new[i])):
                new[i][j] =  new[i][j]**2

        return new
