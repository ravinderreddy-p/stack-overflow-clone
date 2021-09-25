from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from src.add_answer import AddAnswer
from src.add_question import AddQuestion
from src.add_user import AddUser

from src.models import setup_db, User, db, Question, Answer
from src.update_question import UpdateQuestion

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


@app.route('/api/question/create', methods=['POST'])
def post_question():
    req_body = request.get_json()
    question = AddQuestion().add_a_question(req_body)
    return jsonify({
        'success': True,
        'status': 200,
        'message': question.title + ' added successfully'
    })


@app.route('/api/question/<int:id>/edit', methods=['POST'])
def edit_question(id):
    req_body = request.get_json()
    status_code = UpdateQuestion().update_question(req_body, id)
    if status_code == 404:
        abort(404)

    return jsonify({
        'success': True,
        'status': 200,
        'message': 'Question updated successfully'
    })


@app.route('/api/question/<int:id>/answer', methods=['POST'])
def add_answer(id):
    req_body = request.get_json()
    answer = AddAnswer().add_answer(req_body, id)
    return jsonify({
        'success': True,
        'status': 200,
        'message': 'Answered successfully.'
    })