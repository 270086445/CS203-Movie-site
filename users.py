import sqlite3

conn = sqlite3.connect('users.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE users(
                userID integer PRIMARY KEY,
                username text,
                user_password text
                )"""
c.exucute(sql_query)
