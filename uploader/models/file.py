from uuid import uuid4

from sqlalchemy.orm import backref

from models import db


class File(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    upload_file_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship(
        "User",
        foreign_keys=user_id,
        lazy="select",
        backref=backref("files", lazy="dynamic"),
    )

    def __init__(self, user, file_name: str):
        extension = file_name.split(".")[-1]

        self.user = user
        self.file_name = file_name
        self.upload_file_name = (
            str(user.id) + "-" + str(uuid4().hex) + "." + extension
        )

    def delete(self):
        db.session.delete(self)
