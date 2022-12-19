#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[count], end="")
            count += 1
    except IndexError:
        print("Accessed index is out of range")
    finally:
        print()
        return count