#!/usr/bin/python3
"""
python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen, Request

if __name__ == "__main__":
    request = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(request) as rsp_obj:
        obj = rsp_obj.read()
        obj_d = obj.decode("utf-8")

        print("Body response:")
        print("\t- type: {}".format(type(obj)))
        print("\t- content: {}".format(obj))
        print("\t- utf8 content: {}".format(obj_d))
