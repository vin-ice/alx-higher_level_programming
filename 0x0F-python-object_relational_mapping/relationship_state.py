#!/usr/bin/python3
"""
Contains class definition of a State and its instance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class State(Base):
    """
    State class
    """
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement='auto',
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state",
                          cascade="all, delete, delete-orphan")
