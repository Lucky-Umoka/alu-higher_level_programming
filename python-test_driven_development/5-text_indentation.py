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
    stripped = text.strip()
    for i, char in enumerate(stripped):
        result += char
        if char in ".?:" and (i + 1 >= len(stripped) or
                               stripped[i + 1] == " "):
            result += "\n\n"
    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines), end="")
