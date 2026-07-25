#!/usr/bin/python3
"""Module that defines a matrix_divided function.

This module provides a function to divide all elements of a matrix
by a given divisor, returning a new matrix with rounded values.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div.
    """
    is_matrix = isinstance(matrix, list) and len(matrix) > 0
    if is_matrix:
        is_matrix = all(isinstance(row, list) for row in matrix)
    if not is_matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for elem in row:
            valid = isinstance(elem, (int, float))
            valid = valid and not isinstance(elem, bool)
            if not valid:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
