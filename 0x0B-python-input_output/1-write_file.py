#!/usr/bin/python3
"""Implementation of the write_file module"""


def write_file(filename="", text=""):
    """writes text to a file.

    Args:
        filename (file): file to be written to
        text (string): string to be written

    Returns:
        int: number of characters written.

    """
    with open(filename, "w") as myfile:
        myfile.write(text)
        return myfile.tell()
