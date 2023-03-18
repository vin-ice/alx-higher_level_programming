#!/usr/bin/python3
"""
Prints state with the given name
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    args = argv[4]
    state = session.query(State).filter(State.name == args).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
