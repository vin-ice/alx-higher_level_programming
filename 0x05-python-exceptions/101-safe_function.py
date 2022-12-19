#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely
    """
    results = None
    try:
        results = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
    finally:    
        return results