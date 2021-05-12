from models import Deletable
from models import db
from utils.exception import ClientError


class Folder(db.Model, Deletable):
    __tablename__ = "folders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False, default="")
    parent_id = db.Column(db.Integer, db.ForeignKey("folders.id"))

    user = db.relationship("User", foreign_keys=user_id)
    parent = db.relationship(
        "Folder", remote_side=id, uselist=False, backref="children"
    )
    files = db.relationship("File", back_populates="folder")

    def __init__(self, user_id: int, name: str, parent_id: int = None) -> None:
        self.user_id = user_id
        self.name = name
        self.parent_id = parent_id

    def serialize(self) -> dict:
        return {"id": self.id, "name": self.name, "parent_id": self.parent_id}

    def update(self, **kwargs) -> None:
        self.name = kwargs.get("name", self.name)


def create_folder(user, name: str, parent_id: int) -> Folder:
    folder = Folder(user_id=user.id, name=name, parent_id=parent_id)
    db.session.add(folder)
    db.session.flush()
    return folder


def get_folder_by_id(folder_id: int) -> Folder:
    folder = Folder.query.get(folder_id)
    if folder is None:
        raise ClientError("Folder not exist")
    return folder
