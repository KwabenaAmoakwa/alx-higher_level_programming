#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""add_item module"""


if len(sys.argv) < 2:
    save_to_json_file([], "add_item.json")
    sys.exit(1)
data = load_from_json_file("add_item.json")
data += sys.argv[1:]
save_to_json_file(data, "add_item.json")
