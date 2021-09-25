from src.models import Question, db


class UpdateQuestion(object):
    def __init__(self):
        pass

    def update_question(self, request_body, question_id):
        title = request_body.get('title')
        content = request_body.get('content')
        tags = request_body.get('tags')
        user_id = request_body.get('user_id')
        question = Question.query.get(question_id)
        if question.user_id != user_id:
            return 404

        if title != question.title:
            question.title = title

        if content != question.body:
            question.body = content

        if tags != question.tags:
            question.tags = tags
        db.session.commit()
        return 200
