#!/usr/bin/python3
"""
query server with the resquest module
"""

import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    content = res.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
