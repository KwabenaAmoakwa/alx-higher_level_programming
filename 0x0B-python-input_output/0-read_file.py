#!/usr/bin/python3
"""implementation of read_file module"""


def read_file(filename=""):
    """reads files and prints content to stdout.

    Args:
        filename (file): file to be read

    Returns:
        None
    """
    with open(filename) as myfile:
        print(myfile.read(), end="")
