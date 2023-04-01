#!/usr/bin/python3
"""
Sends POST tp http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        res = response.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
