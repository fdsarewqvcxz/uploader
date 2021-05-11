from models import db


class Folder(db.Model):
    __tablename__ = "folders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False, default="")
    parent_id = db.Column(db.Integer, db.ForeignKey("folders.id"))

    user = db.relationship("User", foreign_keys=user_id)
    parent = db.relationship("Folder", foreign_keys=parent_id)

    def __init__(self, user_id: int, name:str, parent_id: int = None):
        self.user_id = user_id
        self.name = name
        self.parent_id = parent_id
