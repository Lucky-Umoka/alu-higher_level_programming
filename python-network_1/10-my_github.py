#!/usr/bin/python3
"""Module that displays a GitHub user's id using Basic Authentication."""
import requests
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
