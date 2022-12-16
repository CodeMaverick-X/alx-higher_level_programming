#!/usr/bin/python3
"""
takes in url and email, sends post request to the passed url
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {"email": email}

    obj_e = urlencode(values)
    obj_ee = obj_e.encode("ascii")
    request = Request(url, obj_ee)

    with urlopen(request) as responds:
        obj = responds.read()
        obj_d = obj.decode("utf-8")
        print(obj_d)
