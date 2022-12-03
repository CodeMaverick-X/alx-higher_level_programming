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
    engine = create_engine(url, echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()
    name = "Louisiana"
    state = State(name=name)
    Base.metadata.create_all(engine)
    new_state = session.query(State).filter(State.name == name).first()
    print("{}".format(new_state.id))
