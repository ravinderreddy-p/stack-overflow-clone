from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from src.add_question import AddQuestion
from src.add_user import AddUser

from src.models import setup_db, User, db, Question

app = Flask(__name__)
setup_db(app)
CORS(app, resources={r"/api/*": {"origins": '*'}})


@app.route('/')
def hell_world():
    return "Hello world!"


@app.route('/api/addUser', methods=['POST'])
def add_user():
    body = request.get_json()
    username = AddUser().create_a_user(body)
    return jsonify({
        'user': username,
        'success': True
    })


@app.route('/api/authenticate', methods=['GET', 'POST'])
def authenticate():
    body = request.get_json()
    username = body['username']
    user = User.query.filter_by(name=username).one_or_none()

    if user is None:
        abort(404)

    return jsonify({
        'success': True,
        'status': 200,
        'message': username + ' Authenticated successfully'
    })


@app.route('/api/question', methods=['POST'])
def post_question():
    req_body = request.get_json()
    question = AddQuestion().add_a_question(req_body)
    return jsonify({
        'success': True,
        'status': 200,
        'message': question.title + ' added successfully'
    })