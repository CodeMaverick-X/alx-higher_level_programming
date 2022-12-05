#!/usr/bin/python3
"""
prints all city obj from the database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, relationship

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost:3306/{}"\
        .format(username, password, database)
    engine = create_engine(url, echo=False)

    session = Session(bind=engine)

    State.cities = relationship("City", order_by=City.id,
                                backref="state")

    cities = session.query(City).join(State).order_by(City.id).all()

    for i, city in enumerate(cities):
        print("{}: ({:d}) {}".format(city.state.name, i+1, city.name))
