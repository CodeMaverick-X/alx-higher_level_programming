#!/usr/bin/python3
"""
script that prints the first State object from the database
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

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    engine = create_engine(url, echo=False)
    hi = engine.execute("select * from states ORDER BY id ASC")
    me = hi.fetchone()

    if me:
        print("{}: {}".format(me[0], me[1]))
    else:
        print()
