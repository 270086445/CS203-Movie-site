import sqlite3

conn = sqlite3.connect('roles.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE roles(
                roleID integer PRIMARY KEY,
                role_name text
                )"""
c.exucute(sql_query)
