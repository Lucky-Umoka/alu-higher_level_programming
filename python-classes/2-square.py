#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """A class that defines a square with validated size."""

    def __init__(self, size=0):
        """Initialize square with optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
