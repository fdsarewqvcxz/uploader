from datetime import datetime

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from models import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __init__(self, name: str, password: str):
        self.name = name
        self.set_password(password)

    def set_password(self, password: str):
        self.password = generate_password_hash(password, "pbkdf2:sha256")

    def check_password(self, password: str):
        return check_password_hash(self.password, password)
