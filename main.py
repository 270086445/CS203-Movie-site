from flask import Flask, request

app = Flask(__name__)


def db_connect():
    conn = None


@app.route('/')
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
