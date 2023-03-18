#!/usr/bin/python3
"""
    SAFE select of passed argument on hbtn_0e_0_usa 
"""
from sys import argv
import MySQLdb

def main():
    """
    SAFE select of passed argument on hbtn_0e_0_usa 
    """
    conn = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3], host="localhost", port=3306, charset="utf8")
    cursor = conn.cursor()
    stmnt = """SELECT * FROM states WHERE name = %s ORDER BY id ASC"""
    args = argv[4]
    cursor.execute(stmnt, (args, ))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()