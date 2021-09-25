from sqlalchemy.orm import relationship

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# database_name = 'sof-clone'
from sqlalchemy import Column, Integer, String, ForeignKey

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

    def __init__(self, name):
        self.name = name


class Question(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String, nullable=False)
    body = db.Column(String, nullable=False)
    tags = db.Column(String, nullable=False)
    user_id = db.Column(Integer, ForeignKey('user.id'))
