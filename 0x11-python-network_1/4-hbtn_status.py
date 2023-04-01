#!/usr/bin/python3
"""
Fetched status
"""
import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body Response:\n\t- type: {}\n\t- content: {}"
          .format(type(res.text), res.text))
