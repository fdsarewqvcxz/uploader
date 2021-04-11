from flask_jwt_extended import create_access_token

from models import db
from models.user import User


class UserController:
    @staticmethod
    def create_user(username: str, password: str):
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {"new_user": new_user.id}

    @staticmethod
    def auth(username: str, password: str):
        user = User.query.filter_by(username=username).one_or_none()
        if user is None:
            raise Exception("User not found")
        if not user.check_password(password):
            raise Exception("Password error")
        access_token = create_access_token(identity=user)
        return {"access_token": access_token}
