from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app) -> None:
    db.init_app(app)


class Deletable:
    def delete(self) -> None:
        db.session.delete(self)


from .file import *
from .user import *
from .folder import *
