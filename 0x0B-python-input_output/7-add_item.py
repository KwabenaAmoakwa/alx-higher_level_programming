#!/usr/bin/python3
"""add_item module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

if len(sys.argv) < 2:
    sys.exit(1)
newlist += sys.argv[1:]
save_to_json_file(newlist, "add_item.json")
