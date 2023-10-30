#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): The matrix to be divided, must be a list of lists of
        integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the elements divided by the divisor.

    Raises:
        TypeError: If the divisor is not a number or if the matrix is not a
        list of lists of integers or floats.
        ZeroDivisionError: If the divisor is zero.
        TypeError: If each row of the matrix does not have the same size.

    """
    d, c = True, True
    li, li1, li2 = [], [], []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")

        li2 += [len(matrix[i])]
        for x in matrix[i]:
            if not type(x) is int and not type(x) is float:
                raise TypeError("matrix must be a matrix (list\
                    of lists) of integers/floats")
            else:
                li += [round((x / div), 2)]
        li1 += [li]
        li = []

    c = all(x == li2[0] for x in li2)
    if c is False:
        raise TypeError("Each row of the matrix must have the same size")
    return li1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
