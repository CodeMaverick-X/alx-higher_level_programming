#!/usr/bin/python3
"""
module to create class for table
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    engine = create_engine(url, echo=False)

    session = Session(bind=engine)

    rows = session.query(State).filter(State.name.like('%a%')).all()

    for row in rows:
        session.delete(row)

    session.commit()
