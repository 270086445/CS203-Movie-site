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


@app.route('/movies', methods=['POST', 'GET'])
def view_movies():
    if request.method == 'GET':
        conn = db_connect()
        c = conn.cursor()
        sql_query = "SELECT * FROM movies"
        c.execute(sql_query)
        movies = c.fetchall()
        return render_template('index.html', movies_data = movies)
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
