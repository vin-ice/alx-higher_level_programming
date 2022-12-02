#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    temp = [0] * (size - 1)
    pos = 0
    for index, item in enumerate(my_list):
        if index == idx:
            continue
        temp[pos] = item
        pos += 1
    my_list.clear()
    for item in temp:
        my_list.append(item)
    return my_list
