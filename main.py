import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

class Movie():
    id = db.Colmn(db.Integer,)


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect("admin.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route('/add', methods=['POST', 'GET'])
def add_movies():
    if request.method == 'GET':
        return 'movies'
    elif request.method == 'POST':
        conn = db_connect()
        c = conn.cursor()
        title = request.form['title']
        year = request.form['year']
        genre = request.form['genre']
        director = request.form['director']
        rating = request.form['rating']
        sql_query = "INSERT INTO movies (title, year, genre, director, rating) VALUES (?,?,?,?,?)"
        c.execute(sql_query, (title, year, genre, director, rating))
        conn.commit()
        return "Added movie!"


def load_movies():
    conn = db_connect()
    c = conn.cursor()
    sql_query = "SELECT * FROM movies"
    c.execute(sql_query)


@app.route('/movies', methods=['GET'])
def view_movies():
    load_movies()
    movies = Movie.query.all()
    return render_template('index.html', movies_data=movies)


@app.route('/display', methods=['GET'])
def show_movies(c):
    load_movies()
    info = c.fetchall()
    return render_template('showcase.html', movies_data=info)


if __name__ == '__main__':
    app.run(debug=True)
