import sqlite3

conn = sqlite3.connect('admin.sqlite')

c = conn.cursor()
sql_query_movies = """CREATE TABLE if not exists movies(
               movieId integer PRIMARY KEY,
               title text,
               year integer,
               director text,
               genre text,
               rating text
               )"""

c.execute(sql_query_movies)

sql_query_users = """CREATE TABLE if not exists users(
                userID integer PRIMARY KEY,
                username text,
                user_role text,
                email text
                )"""
c.execute(sql_query_users)

sql_query_credentials = """CREATE TABLE if not exists credentials(
                credentialID integer PRIMARY KEY,
                userID integer,
                password text
                )"""
c.execute(sql_query_credentials)

sql_query_roles = """CREATE TABLE if not exists roles(
                roleID integer PRIMARY KEY,
                role_name text
                )"""
c.execute(sql_query_roles)

sql_query_relationship = """CREATE TABLE if not exists user_roles(
                userID integer PRIMARY KEY,
                roleID integer
                )"""
c.execute(sql_query_relationship)
