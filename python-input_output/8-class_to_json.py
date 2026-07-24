#!/usr/bin/python3
"""Module that defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of a simple object for JSON."""
    return obj.__dict__
