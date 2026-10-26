#!/usr/bin/python3

"""
a MySQLdb select all accepting arguments from terminal.
"""
if __name__ == "__main__":
    import sys
    db_name = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC") # SQL script
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

        

