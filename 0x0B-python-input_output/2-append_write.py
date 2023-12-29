#!/usr/bin/python3
"""Implementation of the append_write module"""


def append_write(filename="", text=""):
    """appends text to the existing file.

    Args:
        filename (file): file to be appended
        text (string): content to append

    Returns:
        int: the number of characters added
    """
    with open(filename, "a") as myfile:
        myfile.write(text)
        return myfile.tell()
