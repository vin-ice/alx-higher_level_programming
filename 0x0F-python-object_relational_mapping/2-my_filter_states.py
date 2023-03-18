#!/usr/bin/python3
"""
Takes an argument and displays all values in the states table hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def main():
    conn = MySQLdb.connect(user=argv[1],
                           password=argv[2],
                           database=argv[3],
                           host="localhost",
                           port=3306,
                           charset="utf8")

    cursor = conn.cursor()
    cursor.execute("SELECT * from states WHERE\
                   name LIKE %s ORDER BY id ASC", [argv[4]])
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
