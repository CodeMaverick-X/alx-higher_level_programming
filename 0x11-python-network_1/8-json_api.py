#!/usr/bin/python3
"""
get result in json
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    query = ""
    if len(argv) > 1:
        query = argv[1]
    res = requests.post(url, data={'q': query})

    try:
        data = res.json()
        if len(data):
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError as error:
        print("Not a valid JSON")
