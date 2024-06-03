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


@app.route('/movies', methods=["GET"])
def view_movies():
    conn = db_connect()
    c = conn.cursor()
    sql_query = "SELECT * FROM movies"
    c.execute(sql_query)
    movies = c.fetchall()
    return render_template("index.html", movies_data=movies)


@app.route('/add_movie', metohds=["POST", "GET"])
def handle_movies():
    if request.method == "GET":
        return render_template("add_movie.html")
    elif request.method == "POST":
        conn = db_connect()
        c = conn.cursor()
        conn.commit()
        return "Data Saved"


if __name__ == '__main__':
    app.run(debug=True)
