"""Scratch lifecycle v2 e2e fixture. Not imported anywhere."""
import sqlite3


def find_user(conn: sqlite3.Connection, name: str):
    return conn.execute(f"SELECT * FROM users WHERE name = '{name}'").fetchall()
