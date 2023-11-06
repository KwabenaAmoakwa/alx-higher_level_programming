#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a particular class or its subclass.

    Args:
        obj: An object to be checked.
        a_class: A class to check against.

    Returns:
        bool: True if the object is an instance of the class or its subclass,
        False otherwise.
    """
    if a_class == object:
        return False
    return isinstance(obj, a_class)
