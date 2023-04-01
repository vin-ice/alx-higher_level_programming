#!/usr/bin/python3
"""
Sends a POST request and displays the body of res
"""
import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    req = request.Request(sys.argv[1],
                          parse.urlencode(data).encode("ascii"))

    with request.urlopen(req) as response:
        res = response.read()
        print("{}".format(res.decode("utf-8")))
