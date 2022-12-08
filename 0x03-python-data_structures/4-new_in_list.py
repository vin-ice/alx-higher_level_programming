#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    list_temp = my_list.copy()
    if idx < 0 or idx > size - 1:
        return list_temp
    list_temp[idx] = element
    return list_temp