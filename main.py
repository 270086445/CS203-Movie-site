import sqlite3
from flask import Flask, request


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
