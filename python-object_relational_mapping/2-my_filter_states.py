#!/usr/bin/python3
"""Script that lists states matching a name from hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = BINARY '{}' " \
        "ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
