import sqlite3

conn = sqlite3.connect('admin.sqlite')

c = conn.cursor()
sql_query = """CREATE TABLE admin account (
                adminID integer PRIMARY KEY,
                admin_account_name text,
                admin_password text,
                admin_access text,
                )"""
c.exucute(sql_query)