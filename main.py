from flask import Flask, jsonify
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
    role_id = db.relationship('Role', backref='user')

    def __init__(self, username, password, email, role_id):
        self.username = username
        self.password = password
        self.email = email
        self.role_id = role_id


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


@app.route('/get-movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    output = []

    for movie in movies:
        movie_data = {'title': movie.title,
                      'director': movie.director,
                      'genre': movie.genre,
                      'year': movie.year,
                      'rating': movie.rating}
        output.append(movie_data)

    return jsonify({'movies': output}), 200


@app.route('/get-users-by-role/<role_id>', methods=['GET'])
def get_users_by_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    users = Role.query.filter_by(role_id=role_id)
    output = []

    for user in users:
        user_data = {'username': user.username, 'role': user.role_id}
        output.append(user_data)

    return jsonify({'users': output}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
