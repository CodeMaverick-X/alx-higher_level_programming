#!/usr/bin/python3
"""
prints all city obj from the database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    engine = create_engine(url, echo=True)

    session = Session(bind=engine)
    city_obj = session.query(City, State).\
        join(State, State.id == City.state_id).all()

    for i, row in enumerate(city_obj):
        print("{}: ({}) {}".format(row[1].name, i+1, row[0].name))
