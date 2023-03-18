#!/usr/bin/python3
"""
Creates the State California with city San Francisco
    from hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    s = State(name="California")
    c = City(name="San Francisco")
    s.cities = [c]

    session.add(s)
    session.commit()
    session.close()