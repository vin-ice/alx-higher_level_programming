#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    temp_list = [0] * list_length
    for i in range(list_length):
        try:
            temp_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            pass
        except ZeroDivisionError:
            print("division by 0")
            pass
        except IndexError:
            print("out of range")
            pass
    return temp_list 
