#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        response = res.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- "
              "utf8 content: {}"
              .format(type(response), response, response.decode("utf-8")))
