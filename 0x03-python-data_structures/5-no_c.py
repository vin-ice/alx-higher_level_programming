#!/usr/bin/python3
def no_c(my_string):
    str_temp = []
    for char in my_string:
        if char == 'c' or char == 'C':
            char = ''
        str_temp.append(char)
    return "".join(str_temp)
