#!/usr/bin/python3
"""
Lists all states from  database hbtn_0e_usa
"""
from sys import argv
import MySQLdb

def main():
    """
    Lists all states from  database hbtn_0e_usa
    """
    conn = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3], host="localhost", port=3306, charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * from states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()