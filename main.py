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


if __name__ == '__main__':
    app.run(debug=True)
