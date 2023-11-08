#!/usr/bin/python3
"""Implementation of to_json_string module"""
import json


def to_json_string(my_obj):
    """converts object ot json format.

    Args:
        my_obj (object): object

    Returns:
        json
    """
    data = json.dumps(my_obj)
    return data
