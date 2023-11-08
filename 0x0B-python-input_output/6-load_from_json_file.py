#!/usr/bin/python3
"""Implementation of the load_from_json_file module"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”.

    Args:
        filename (file): file

    Returns:
        None
    """
    with open(filename) as myfile:
        data = json.load(myfile)
        return data
