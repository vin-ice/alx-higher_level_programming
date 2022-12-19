#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        return {k: a_dictionary[k] * 2 for k in a_dictionary}