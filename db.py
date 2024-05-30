import sqlite3

conn = sqlite3.connect('admin.sqlite')

c = conn.cursor()
sql_query_movies = """CREATE TABLE movies(
               movieId integer PRIMARY KEY,
               title text,
               year integer,
               director text,
               genre text,
               rating text
               )"""

c.execute(sql_query_movies)

sql_query_users = """CREATE TABLE users(
                userID integer PRIMARY KEY,
                username text,
                user_role text,
                email text
                )"""
c.exucute(sql_query_users)

sql_query_credentials = """CREATE TABLE credentials(
                credentialID integer PRIMARY KEY,
                userID integer,
                password text
                )"""
c.exucute(sql_query_credentials)

sql_query_roles = """CREATE TABLE roles(
                roleID integer PRIMARY KEY,
                role_name text
                )"""
c.exucute(sql_query_roles)

sql_query_relationship = """CREATE TABLE relationship between admins users and movies (
                userID integer PRIMARY KEY,
                roleID integer
                )"""
c.exucute(sql_query_relationship)

