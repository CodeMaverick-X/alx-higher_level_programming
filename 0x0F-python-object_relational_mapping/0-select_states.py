#!/usr/bin/python3

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]
f = 0

db = MySQLdb.connect(host="localhost", port=3306,user=username, passwd=password, db=database)


c = db.cursor()

c.execute("select * from states")
result = c.fetchall()

for i in result:
    print(i)
