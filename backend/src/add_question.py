from src.models import Question, db


class AddQuestion(object):
    def __init__(self):
        pass

    def add_a_question(self, request_body):
        title = request_body.get('title')
        content = request_body.get('content')
        tags = request_body.get('tags')
        user_id = request_body.get('user_id')
        question = Question(title=title, body=content, tags=tags, user_id=user_id)
        db.session.add(question)
        db.session.commit()
        return question
