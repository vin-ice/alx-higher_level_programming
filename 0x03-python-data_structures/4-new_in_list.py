#!/usr/bin/python3
size = 0
list_temp = []
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0 or idx > size - 1:
        return my_list
    list_temp = my_list
    list_temp[idx] = element
    return list_temp
