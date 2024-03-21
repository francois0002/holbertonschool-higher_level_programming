#!/usr/bin/python3
"""
Module list state where name start with N
"""
import sys
import MySQLdb


def main():
    """ sonction list state where name start with N """
    connection = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_row = cur.fetchall()
    for states in query_row:
        print(states)
    cur.close()
    connection.close()


if __name__ == "__main__":
    main()
