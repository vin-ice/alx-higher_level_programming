#!/usr/bin/python3
size = 0
def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0 or idx > size - 1:
        return my_list
    my_list[idx] = element
    return my_list
