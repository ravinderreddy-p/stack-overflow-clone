from src.models import User, db


class AddUser(object):
    def __init__(self):
        pass

    def create_a_user(self, request_body):
        username = request_body.get('username')
        user = User(name=username)
        db.session.add(user)
        db.session.commit()
        return username
