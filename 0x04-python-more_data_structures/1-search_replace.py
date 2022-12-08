#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = []
    for index, item in enumerate(my_list):
        if index + 1 == search:
            item = replace
        temp.append(item)
    return temp
