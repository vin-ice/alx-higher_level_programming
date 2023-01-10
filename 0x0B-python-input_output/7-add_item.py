#!/usr/bin/python3
"""Module with args saver"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_file = "add_item.json"
if os.path.exists(my_file) and os.path.getsize(my_file) > 0:
    save_to_json_file((load_from_json_file(my_file) + sys.argv[1:]), my_file)
else:
    save_to_json_file([], my_file)

