#!/usr/bin/python3
"""Module that defines an add_integer function.

This module provides a single function to add two numbers together,
after validating and casting them to integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats, casting floats to integers first.

    Args:
        a (int/float): The first number.
        b (int/float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
