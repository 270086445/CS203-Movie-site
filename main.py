import sqlite3
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    director = db.Column(db.String)
    genre = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.String)

    def __init__(self, title, director, genre, year, rating):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.rating = rating


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


class Role(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String)
    users = db.relationship('User', backref='role')


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
