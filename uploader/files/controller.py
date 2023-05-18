import io
from typing import Tuple

import boto3
from flask import current_app
from models import create_file, db, get_file_by_id
from utils.exception import ForbiddenError


class FileController:
    @staticmethod
    def create_file(
        access_user, file: bytes, filename: str, folder_id: int
    ) -> dict:
        new_file = create_file(
            user=access_user, filename=filename, folder_id=folder_id
        )

        s3 = boto3.resource(
            "s3",
            aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        )
        s3.Bucket("uploaderfiles").put_object(
            Key=f"{new_file.user_id}/{new_file.uploaded_name}", Body=file
        )

        db.session.commit()
        return {"file_id": new_file.id}

    @staticmethod
    def get_file(access_user, file_id: int) -> Tuple[io.BytesIO, str]:
        file = get_file_by_id(file_id)
        if access_user.id != file.user_id:
            raise ForbiddenError
        s3 = boto3.resource(
            "s3",
            aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        )

        buffer = io.BytesIO()
        s3.Bucket("uploaderfiles").download_fileobj(
            f"{file.user_id}/{file.uploaded_name}", buffer
        )
        buffer.seek(0)
        return buffer, file.name

    @staticmethod
    def delete_file(access_user, file_id: int) -> dict:
        file = get_file_by_id(file_id)
        if access_user.id != file.user_id:
            raise ForbiddenError

        file.delete()

        s3 = boto3.resource(
            "s3",
            aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        )
        obj = s3.Object("uploaderfiles", f"{file.user_id}/{file.uploaded_name}")
        obj.delete()
        db.session.commit()
        return {"success": True}
