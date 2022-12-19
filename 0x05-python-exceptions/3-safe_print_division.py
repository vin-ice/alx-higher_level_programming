#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the results
    """
    div = None
    try:
        div = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result {}".format(div))
        return div