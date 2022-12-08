#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    k, v = list(a_dictionary.items())[0]
    for key, val in a_dictionary.items():
        if val > v:
            k, v = key, val
    return k
