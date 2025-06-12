from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, User, Post

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app, db)

# initialize the app with the extension
db.init_app(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is about us page"

@app.route("/<username>")
def username(username):
    return f'Hello {username}'

@app.route('/posts')
def posts():
    # list of python dictionary
    posts = [post.to_dict() for post in Post.query.all()]

    return make_response(posts)
    


if __name__ == '__main__':
    app.run(debug=True, port=4000)


















