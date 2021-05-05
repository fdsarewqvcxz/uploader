from flask_jwt_extended import create_access_token

from models import db
from models import Folder
from models import User
from utils.exception import ClientError


class UserController:
    @staticmethod
    def create_user(name: str, password: str):
        new_user = User(name=name, password=password)
        db.session.add(new_user)
        db.session.flush()

        root_folder = Folder(user_id=new_user.id, name="root")
        db.session.add(root_folder)

        db.session.commit()
        return {"new_user": new_user.id}

    @staticmethod
    def auth(name: str, password: str):
        user = User.query.filter_by(name=name).one_or_none()
        if user is None:
            raise ClientError("User not found")
        if not user.check_password(password):
            raise ClientError("Password error")
        access_token = create_access_token(identity=user)
        return {"access_token": access_token}
