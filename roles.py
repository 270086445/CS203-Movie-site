import sqlite3

conn = sqlite3.connect('roles.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE roles(
                roleID integer PRIMARY KEY,
                role_name text
                )"""
c.execute(sql_query)
