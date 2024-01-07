#!/usr/bin/python3
"""implementation of add_item module"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"save to file module"
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"load to file module"

"""The body of the script"""
if len(sys.argv) < 2:
    """ to check whether there is a command line argument or not"""
    save_to_json_file([], "add_item.json")
    sys.exit(1)
    
data = load_from_json_file("add_item.json")
data += sys.argv[1:]
save_to_json_file(data, "add_item.json")
