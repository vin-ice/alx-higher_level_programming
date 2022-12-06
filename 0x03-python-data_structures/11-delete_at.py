#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    pos = 0
    if idx < 0 or idx > size - 1:
        return my_list
    temp = my_list.copy()
    my_list.clear()
    for index, item in enumerate(temp):
        if index == idx:
            continue
        my_list.append(item)
    return my_list