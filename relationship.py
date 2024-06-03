import sqlite3

conn = sqlite3.connect('relationship.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE relationship between admins users and movies (
                userID integer PRIMARY KEY,
                roleID integer
                )"""
c.execute(sql_query)
