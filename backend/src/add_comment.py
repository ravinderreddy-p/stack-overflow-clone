from src.models import db, Comment


class AddComment(object):
    def __init__(self):
        pass

    def comment_to_question(self, request_body, question_id):
        text = request_body.get('comment')
        user_id = request_body.get('user_id')
        comment = Comment(text=text, user_id=user_id, question_id=question_id)
        db.session.add(comment)
        db.session.commit()
        return comment

    # def comment_to_answer(self, request_body, answer_id):
    #     text = request_body.get('comment')
    #     user_id = request_body.get('user_id')
    #     comment = Comment(text=text, user_id=user_id, answer_id=answer_id)
    #     db.session.add(comment)
    #     db.session.commit()
    #     return comment
