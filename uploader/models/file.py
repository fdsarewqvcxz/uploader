from uuid import uuid4

from models import Deletable
from models import db
from utils.exception import ClientError


class File(db.Model, Deletable):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    uploaded_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    folder_id = db.Column(
        db.Integer, db.ForeignKey("folders.id"), nullable=False
    )

    user = db.relationship("User", foreign_keys=user_id)
    folder = db.relationship("Folder", foreign_keys=folder_id, lazy="select")

    def __init__(self, user_id, name: str, folder_id: int):
        extension = name.split(".")[-1]

        self.user_id = user_id
        self.name = name
        self.uploaded_name = (
            str(user_id) + "-" + str(uuid4().hex) + "." + extension
        )
        self.folder_id = folder_id

    def serialize(self):
        return {"id": self.id, "name": self.name}


def create_file(user, filename: str, folder_id: int) -> File:
    file = File(user_id=user.id, name=filename, folder_id=folder_id)
    db.session.add(file)
    db.session.flush()
    return file


def get_file_by_id(file_id: int) -> File:
    file = File.query.get(file_id)
    if file is None:
        raise ClientError("File not exist")
    return file
