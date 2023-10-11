#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nm = []
    for i in range(len(matrix)):
        nm += [[x**2 for x in matrix[i]]]
    return nm
