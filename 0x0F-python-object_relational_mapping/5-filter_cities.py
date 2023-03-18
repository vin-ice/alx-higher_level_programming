#!/usr/bin/python3
"""
Lists all cities of given state in hbtn_0e_04_usa
"""
from sys import argv
from itertools import chain
import MySQLdb


def main():
    """
    Lists all cities of given state in hbtn_0e_04_usa
    """
    conn = MySQLdb.connect(user=argv[1],
                           password=argv[2],
                           database=argv[3],
                           host="localhost",
                           port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    stmt = """SELECT cities.name FROM cities
             INNER JOIN states
             ON cities.state_id = states.id
             WHERE states.name = %s"""
    args = argv[4]
    cursor.execute(stmt, (args, ))
    cities = cursor.fetchall()

    print(', '.join(map(str, chain.from_iterable(cities))))

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
