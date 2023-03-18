#!/usr/bin/python3
"""
Lists all states with a name starting with N from htbn_0e_0_usa
"""
from sys import argv
import MySQLdb

def main():
    """
    Lists all states with a name starting with N from htbn_0e_0_usa
    """
    conn = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3], host="localhost", port=3306, charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * from states WHERE ASCII(left(name, 1)) = ASCII(%s) ORDER BY id ASC", "N")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()