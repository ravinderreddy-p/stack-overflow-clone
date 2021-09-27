from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from src.add_answer import AddAnswer
from src.add_comment import AddComment
from src.add_question import AddQuestion
from src.add_user import AddUser

from src.models import setup_db, User, db, Question, Answer
from src.update_question import UpdateQuestion

app = Flask(__name__)
setup_db(app)
CORS(app, resources={r"/api/*": {"origins": '*'}})


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
#     return response


@app.route('/api/')
def hell_world():
    return jsonify({
        'message': 'Hello World!'
    })


@app.route('/api/addUser', methods=['POST'])
def add_user():
    body = request.get_json()
    username = AddUser().create_a_user(body)
    return jsonify({
        'user': username,
        'success': True
    })


@app.route('/api/authenticate/<string:username>/', methods=['GET'])
def authenticate(username):
    # body = request.get_json()
    # username = body['username']
    user = User.query.filter_by(name=username).one_or_none()

    if user is None:
        return jsonify({
            'success': False,
            'status': 404,
            'username': username,
            'message': username + ' not authorized.'
        })
        # abort(404)

    return jsonify({
        'success': True,
        'status': 200,
        'username': username,
        'id': user.id,
        'message': username + ' Authenticated successfully'
    })


@app.route('/api/questions/add/', methods=['POST'])
def post_question():
    req_body = request.get_json()
    question = AddQuestion().add_a_question(req_body)
    return jsonify({
        'success': True,
        'status': 200,
        'message': question.title + ' added successfully'
    })


@app.route('/api/questions/all/', methods=['GET'])
def get_all_questions():
    questions = AddQuestion().get_all_questions()
    return jsonify({
        'success': True,
        'status': 200,
        'questions': questions
    })


@app.route('/api/questions/<int:id>/edit/', methods=['POST'])
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


@app.route('/api/questions/<int:id>/answer/', methods=['POST'])
def add_answer(id):
    req_body = request.get_json()
    answer = AddAnswer().add_answer(req_body, id)
    return jsonify({
        'success': True,
        'status': 200,
        'message': 'Answered successfully.'
    })


@app.route('/api/questions/<int:id>/comment/', methods=['POST'])
def add_comment(id):
    req_body = request.get_json()
    comment = AddComment().comment_to_question(req_body, id)
    return jsonify({
        'success': True,
        'status': 200,
        'message': 'Commented successfully.'
    })


# @app.route('/api/question/<int:question_id>/answer/<int:answer_id>/comment', methods=['POST'])
# def add_comment(question_id, answer_id):
#     req_body = request.get_json()
#     comment = AddComment().comment_to_answer(req_body, answer_id)
#     return jsonify({
#         'success': True,
#         'status': 200,
#         'message': 'Commented successfully.'
#     })