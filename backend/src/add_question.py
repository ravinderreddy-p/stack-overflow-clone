from src.models import Question, db, Answer, User


class AddQuestion(object):
    def __init__(self):
        pass

    def add_a_question(self, request_body):
        title = request_body.get('title')
        content = request_body.get('body')
        tags = request_body.get('tags')
        user_id = request_body.get('user_id')
        question = Question(title=title, body=content, tags=tags, user_id=user_id)
        db.session.add(question)
        db.session.commit()
        return question

    def get_all_questions(self):
        questions = Question.query.all()
        questions_list = []
        for question in questions:
            question_json = {
                'id': question.id,
                'tags': question.tags,
                'title': question.title,
                'body': question.body
            }
            questions_list.append(question_json)
        return questions_list

    def get_a_question(self, question_id):
        question = Question.query.filter_by(id=question_id).first()
        answers = Answer.query.with_entities(Answer.id, Answer.content, Answer.is_accepted, User.name).\
            join(User, Answer.user_id == User.id).\
            filter(Answer.question_id == question_id).all()
        answer_list = []
        if answers is None:
            answer_list = []
        else:
            for ans in answers:
                ans_json = {
                    'answer_id': ans.id,
                    'answer': ans.content,
                    'isAccepted': ans.is_accepted,
                    'answeredBy': ans.name,
                }
                answer_list.append(ans_json)
        question_json = {
            'id': question.id,
            'title': question.title,
            'body': question.body,
            'tags': question.tags,
            'answers': answer_list
        }
        return question_json
