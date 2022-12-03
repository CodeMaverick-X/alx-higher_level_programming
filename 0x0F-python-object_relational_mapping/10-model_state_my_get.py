#!/usr/bin/python3
"""
module to create class for table
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sys import argv

from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    srch_name = argv[4].split("'\"")

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    engine = create_engine(url, echo=False)

    sql_cmd = "select * from states where name\
        = %s ORDER BY id ASC"
    hi = engine.execute(sql_cmd, (srch_name))
    me = hi.fetchall()

    if me:
        for i in me:
            print("{}".format(i[0]))
    else:
        print("Not found")
