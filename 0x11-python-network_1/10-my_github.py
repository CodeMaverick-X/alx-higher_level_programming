#!/usr/bin/python3
"""
get user id from a github id using the gihub api
using basic authentication
"""


import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))

    if r.status_code == 200:
        print(r.json().get("id"))
    else:
        print("None")
