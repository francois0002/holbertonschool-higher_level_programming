#!/usr/bin/python3
""" This file prints all states from the database """

import MySQLdb
import sys

def main():
    """ script that print all the states when called on """
    connection = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_row = cur.fetchall()
    for states in query_row:
        print(states)
    cur.close()
    connection.close()

if __name__ == '__main__':
    main()
