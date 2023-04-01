#!/usr/bin/python3
"""Takes in a URL and email and sends post to req"""
from sys import argv
import requests

if __name__ == "__main__":
    res = requests.post(argv[1], data={"email": argv[2]})
    print(res.text)
