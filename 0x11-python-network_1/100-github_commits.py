#!/usr/bin/python3
"""
lists 10 commits in a github repo by a given user
"""
from sys import argv
import requests

if __name__ == "__main__":
    q = "{}/{}".format(argv[2], argv[1])
    headers = {}
    headers["Accept"] = "application/vnd.github+json"
    headers["X-GitHub-Api-Version"] = "2022-11-28"

    res = requests.get("https://api.github.com/repos/{}/commits"
                       "?per_page=10"
                       .format(q),
                       headers=headers)

    if res.status_code == 200:
        commits = res.json()[:10]
        for c in commits:
            print("{}: {}".format(c.get("sha"),
                  c.get("commit").get("author").get("name")))
