#!/usr/bin/python3
"""
Lists all cities from hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

def main():
    """
    Lists all cities from hbtn_0e_0_usa
    """
    conn = MySQLdb.connect(user=argv[1],
                           password=argv[2],
                           database=argv[3],
                           host="localhost",
                           port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities, states WHERE cities.state_id = states.id
                    ORDER BY cities.id""")
    cities = cursor.fetchall()

    for city in cities:
        print(city)
    
    cursor.close() 
    conn.close() 

if __name__ == "__main__":
    main()