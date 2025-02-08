from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/")
def index():
    return "Index Page"


@app.route('/user/<username>')
def show_user_profile(username: str):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath: str):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
