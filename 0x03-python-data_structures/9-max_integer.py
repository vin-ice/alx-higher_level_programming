#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    max_i = 0
    if size < 1:
        return None
    for item in my_list:
        if item > max_i:
            max_i = item
    return max_i

