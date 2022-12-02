#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res_list = [False] * len(my_list)
    for index, item in enumerate(my_list):
        if item % 2 == 0:
            res_list[index] = True
    return res_list
