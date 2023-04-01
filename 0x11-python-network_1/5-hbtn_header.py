#!/usr/bin/python3
"""Sends data to URL and displays value of X-Request-Id"""
from sys import argv
import requests


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
