#!/usr/bin/python3
"""
scrip that takes in a url and displays the value of the
x-request-id
"""
from urllib.request import urlopen, Request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = Request(url)
    with urlopen(request) as responds:
        obj = responds.info()["X-Request-Id"]
        print(obj)
