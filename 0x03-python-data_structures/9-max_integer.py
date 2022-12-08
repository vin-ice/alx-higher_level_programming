#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_i = my_list[0]
    for item in my_list:
        if item > max_i:
            max_i = item
    return max_i

