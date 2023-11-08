#!/usr/bin/python3
"""Implementation of the write_file module"""


def write_file(filename="", text=""):
    with open(filename, "w") as myfile:
        myfile.write(text)
        return myfile.tell()
