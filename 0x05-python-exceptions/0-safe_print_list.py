#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for count in range(x):
            print(my_list[count], end="")
    except IndexError:
        print("Accessed index is out of range")
    finally:
        print()
        return count + 1