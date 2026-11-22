import sqlite3

def find_user(conn, name):
    # canary: SQL built by string formatting from caller input
    return conn.execute("SELECT * FROM users WHERE name = %s" % name).fetchall()
