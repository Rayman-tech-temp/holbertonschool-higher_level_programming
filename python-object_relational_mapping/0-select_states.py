#!/usr/bin/python3

"""
a MySQLdb select all accepting arguments from terminal.
"""
if __name__ == "__main__":
    import MYSQLdb
    import sys
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[2],
                           passwd=sys.argv[3],
                           db=sys.argv[1])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
