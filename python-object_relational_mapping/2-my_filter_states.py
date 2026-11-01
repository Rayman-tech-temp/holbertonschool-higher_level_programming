#!/usr/bin/python3
"""
a MySQLdb select all accepting arguments from terminal.
"""
import sys
import MySQLdb
if __name__ == "__main__":

    search = sys.argv[4]
    cur = conn.cursor()
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur.execute("SELECT * 
                FROM states 
                WHERE name 
                LIKE BINARY {}
                ORDER BY states.id".format(search))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
