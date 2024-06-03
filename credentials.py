import sqlite3

conn = sqlite3.connect('credentials.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE credentials(
                credentialID integer PRIMARY KEY,
                userID integer,
                password text
                )"""
c.execute(sql_query)
