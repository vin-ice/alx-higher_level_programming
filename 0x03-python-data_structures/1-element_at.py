#!/usr/bin/python3
size = 0
def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0 or idx > size - 1:
        return "None"
    return my_list[idx]

