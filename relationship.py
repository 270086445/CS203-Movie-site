import sqlite3

conn = sqlite3.connect('relationship.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE relationship between admins users and movies (
                movieID integer PRIMARY KEY,
                admin_account_name text,
                date_posted text,
                users_looked_at_it text,
                )"""
c.exucute(sql_query)