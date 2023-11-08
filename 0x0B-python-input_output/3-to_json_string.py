#!/usr/bin/python3
"""Implementation of to_json_string module"""
import json


def to_json_string(my_obj):
    data = json.dumps(my_obj)
    return data
