from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)


from .file import File
from .user import User
from .folder import Folder
