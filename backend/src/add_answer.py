from src.models import Question, db, Answer


class AddAnswer(object):
    def __init__(self):
        pass

    def add_answer(self, request_body, question_id):
        content = request_body.get('answer')
        user_id = request_body.get('user_id')
        answer = Answer(content=content, user_id=user_id, question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        return answer
