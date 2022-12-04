#!/usr/bin/python3
"""
script that changes the name
of a State object from the database
"""

from sqlalchemy import create_engine
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

    row = session.query(State).filter(State.id == 2).first()
    row.name = "New Mexico"
    session.commit()
