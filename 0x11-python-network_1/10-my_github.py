#!/usr/bin/python3
"""
Gets user's id from github
"""
from sys import argv
import requests

if __name__ == "__main__":
    headers = {}
    headers["Accept"] = "application/vnd.github+json"
    headers["Authorization"] = "Bearer {}".format(argv[2])
    headers["X-GitHub-Api-Version"] = "2022-11-28"

    res = requests.get("https://api.github.com/users/{}".format(argv[1]),
                       headers=headers)

    if res.status_code == 200:
        try:
            print(res.json().get("id"))
        except ValueError as e:
            print(e)
    else:
        print("None")
