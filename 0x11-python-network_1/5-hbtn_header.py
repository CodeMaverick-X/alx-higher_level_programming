#!/usr/bin/python3
"""
takes a url and sends a request and displayes
using requests module
"""

import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    r = requests.get(url)

    tmp = r.headers.get("X-Request-Id")
    print(tmp)
