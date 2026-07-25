#!/usr/bin/python3
"""Module that defines a text_indentation function.

This module provides a function that prints text with 2 new lines
after each occurrence of '.', '?' or ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines).strip("\n"), end="")
