from models import db
from models import create_folder
from models import get_folder_by_id
from utils.exception import ForbiddenError


class FolderController:
    @staticmethod
    def create_folder(access_user, name: str, parent_id: int):
        folder = create_folder(user=access_user, name=name, parent_id=parent_id)
        db.session.commit()
        return {"folder_id": folder.id}

    @staticmethod
    def get_folder(access_user, folder_id: int):
        folder = get_folder_by_id(folder_id)
        if access_user.id != folder.user_id:
            raise ForbiddenError
        return {
            "current_folder": folder.serialize(),
            "child_folders": [f.serialize() for f in folder.children],
            "files": [f.serialize() for f in folder.files],
        }

    @staticmethod
    def update_folder(access_user, folder_id: int, name: str):
        folder = get_folder_by_id(folder_id)
        if access_user.id != folder.user_id:
            raise ForbiddenError
        folder.update(name=name)
        db.session.commit()
        return {"folder_id": folder.id}

    @staticmethod
    def delete_folder(access_user, folder_id: int):
        folder = get_folder_by_id(folder_id)
        if access_user.id != folder.user_id:
            raise ForbiddenError
        folder.delete()
        db.session.commit()
        return {"success": True}
