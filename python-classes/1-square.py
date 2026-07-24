#!/usr/bin/python3
"""Module that defines a Square class with private size."""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize square with size.

        Args:
            size: The size of the square.
        """
        self.__size = size
