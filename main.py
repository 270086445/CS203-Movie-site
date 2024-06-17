import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect("admin.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn


def load_movies():
    conn = db_connect()
    c = conn.cursor()
    sql_query = "SELECT * FROM movies"
    c.execute(sql_query)


@app.route('/movies')
def view_movies(c):
    load_movies()
    movies = c.fetchall()
    return render_template('index.html', movies_data=movies)


@app.route('/display')
def show_movies(c):
    load_movies()
    info = c.fetchall()
    return render_template('showcase.html', movies_data=info)


if __name__ == '__main__':
    app.run(debug=True)
