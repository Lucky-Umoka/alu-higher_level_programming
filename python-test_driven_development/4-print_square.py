#!/usr/bin/python3
"""Module that defines a print_square function.

This module provides a function that prints a square made of the
'#' character, of a given size.
"""


def print_square(size):
    """Print a square of '#' characters of a given size.

    Args:
        size (int): The length of the sides of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
