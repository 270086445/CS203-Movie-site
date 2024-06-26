from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


# Connect to the database
def connect_db():
    return sqlite3.connect('database.db')


# Route to display the form
@app.route('/')
def index():
    return render_template('AddMovies.html')


# Route to handle form submission
@app.route('/add', methods=['POST'])
def submit():
    title = request.form['title']
    year = request.form['year']
    director = request.form['director']
    rating = request.form['rating']
    genre = request.form['genre']

    # Connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute("INSERT INTO movies "
                   "(title, year, director, rating, genre) VALUES (?, ?, ?, ?, ?)",
                   (title, year, director, rating, genre))
    conn.commit()
    conn.close()

    return 'Movie submitted successfully!'


if __name__ == '__main__':
    app.run(debug=True)
