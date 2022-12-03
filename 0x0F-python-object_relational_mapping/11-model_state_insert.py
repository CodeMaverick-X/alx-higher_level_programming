#!/usr/bin/python3
"""
module to create class for table
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    engine = create_engine(url, echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    name = "Louisiana"
    state = State(name=name)
    session.add(state)
    new = session.query(State).filter(State.name == name).first()
    session.commit()
    print("{}".format(new.id))
