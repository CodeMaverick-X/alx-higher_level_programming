#!/usr/bin/python3
"""
module to create class for table
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    class state to represent state table.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


"""url="mysql://reinhard:password@localhost:3306/hbtn_0e_0_usa"
engine = create_engine(url, echo=True)
Base.metadata.create_all(engine)"""
