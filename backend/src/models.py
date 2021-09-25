from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# database_name = 'sof-clone'
from sqlalchemy import Column, Integer, String

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


'''
User
'''


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add()
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'user': self.name
        }
