#!/usr/bin/python3
"""
script that lists all State objects from the database
note i didnt use orm, i used core, USE ORM!!!
"""

from sqlalchemy import create_engine
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
    me = hi.fetchall()
    for i in me:
        print("{}: {}".format(i[0], i[1]))
