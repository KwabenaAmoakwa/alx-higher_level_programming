#!/usr/bin/python3
"""implementatin of save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): object
        filename (file): file

    Returns:
        None
    """
    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
