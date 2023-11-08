#!/usr/bin/python3
"""implementation of from_json_string"""
import json


def from_json_string(my_str):
    """converts json string to object.

    Args:
        my_str (str): string

    Returns:
        object
    """
    data = json.loads(my_str)
    return data
