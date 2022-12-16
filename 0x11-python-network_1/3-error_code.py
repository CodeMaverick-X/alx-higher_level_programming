#!/usr/bin/python3
"""
update
"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    request = Request(url)

    try:
        with urlopen(request) as responds:
            obj = responds.read()
            obj_d = obj.decode("utf-8")
            print("{}".format(obj_d))
    except HTTPError as e:
        print("Error code: {:d}".format(e.code))
