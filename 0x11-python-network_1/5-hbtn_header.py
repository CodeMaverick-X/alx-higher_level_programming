#!/usr/bin/python3
# takes a url and sends a request and displayes
# using requests module

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io")

    tmp = r.headers["X-Request-Id"]
    print(tmp)
