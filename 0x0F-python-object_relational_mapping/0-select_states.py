#!/usr/bin/python3

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]
f = 0
try:
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    f = 1
except Exception:
    print("error acceccing db")
if f == 1:
    c = db.cursor()

    c.execute("select * from states")
    result = c.fetchall()

    for i in result:
        print(i)
