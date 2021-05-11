from uuid import uuid4

from models import db


class File(db.Model):
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

    def __init__(self, user, name: str, folder_id: int):
        extension = name.split(".")[-1]

        self.user = user
        self.name = name
        self.uploaded_name = (
            str(user.id) + "-" + str(uuid4().hex) + "." + extension
        )
        self.folder_id = folder_id

    def delete(self):
        db.session.delete(self)
