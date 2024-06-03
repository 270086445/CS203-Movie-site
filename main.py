import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect("admin.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route('/')
def view_movies():
    conn = db_connect()
    c = conn.cursor()
    sql_query = "SELECT * FROM movies"
    c.execute(sql_query)
    movies = c.fetchall()
    return render_template('index.html', movie_data=movies)


if __name__ == '__main__':
    app.run(debug=True)
