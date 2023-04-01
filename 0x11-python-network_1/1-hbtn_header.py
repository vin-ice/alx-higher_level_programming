#!/usr/bin/python3
"""
Sends request to URL and displays the value if X-request-Id
"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as res:
        print(dict(res.info()).get("X-Request-Id"))
