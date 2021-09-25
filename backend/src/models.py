from sqlalchemy.orm import relationship

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# database_name = 'sof-clone'
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

database_path = 'postgresql://pravinderreddy@localhost:5432/sof-clone'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all()


'''
User
'''


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    posts = relationship('Question', backref='user')
    answers = relationship('Answer', backref='user')

    def __init__(self, name):
        self.name = name


class Question(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String, nullable=False)
    body = db.Column(String, nullable=False)
    tags = db.Column(String, nullable=False)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    answers = relationship('Answer', backref='question')


class Answer(db.Model):
    id = db.Column(Integer, primary_key=True)
    content = db.Column(String, nullable=False)
    is_accepted = db.Column(Boolean)
    question_id = db.Column(Integer, ForeignKey('question.id'))
    user_id = db.Column(Integer, ForeignKey('user.id'))