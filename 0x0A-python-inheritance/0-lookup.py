#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """lookup returns the list of available attributes and methods of an
    object.

    Args:
        obj (any): any class type can be passed

    Returns:
        list of attributes and methods"""
    return dir(obj)
