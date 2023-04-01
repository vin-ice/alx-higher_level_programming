#!/usr/bin/python3
"""
sends request to url and displays body
"""
from sys import argv
from urllib import request
from urllib import error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print("{}".format(res.read().decode("utf-8")))
    except error.HTTPError as e:
        print("Error Code: {}".format(e.code))
