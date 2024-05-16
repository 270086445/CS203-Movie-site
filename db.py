import sqlite3

conn = sqlite3.connect('movies.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE movies (
               movieId integer PRIMARY KEY,
               title text,
               year integer,
               director text,
               genre text,
               rating text
               )"""
c.execute(sql_query)
