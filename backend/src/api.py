from flask import Flask, request, jsonify
from flask_cors import CORS

from src.models import setup_db, User, db

app = Flask(__name__)
setup_db(app)
CORS(app, resources={r"/api/*": {"origins": '*'}})


@app.route('/')
def hell_world():
    return "Hello world!"


@app.route('/api/addUser', methods=['POST'])
def add_user():
    body = request.get_json()
    user_name = body.get('username')
    user = User(name=user_name)
    db.session.add(user)
    db.session.commit()
    # user.insert()
    return jsonify({
        "user": user_name,
        "success": "true"
    })


@app.route('/api/authenticate', methods=['GET', 'POST'])
def authenticate():
    return "User authenticated"

