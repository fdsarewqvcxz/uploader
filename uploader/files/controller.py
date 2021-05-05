import io
from typing import Tuple

import boto3
from flask import current_app

from models import db
from models.file import File
from utils.exception import ClientError
from utils.exception import ForbiddenError


class FilesController:
    @staticmethod
    def create_file(access_user, file) -> dict:
        new_file = File(user=access_user, file_name=file.filename)
        db.session.add(new_file)
        db.session.flush()

        s3 = boto3.resource(
            "s3",
            aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        )
        s3.Bucket("uploaderfiles").put_object(
            Key=f"{new_file.user_id}/{new_file.upload_file_name}", Body=file
        )

        db.session.commit()
        return {"file_id": new_file.id}

    @staticmethod
    def get_file(access_user, file_id: int) -> Tuple[io.BytesIO, str]:
        file = File.query.get(file_id)
        if file is None:
            raise ClientError("File not exist")
        if access_user.id != file.user_id:
            raise ForbiddenError
        s3 = boto3.resource(
            "s3",
            aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        )

        buffer = io.BytesIO()
        s3.Bucket("uploaderfiles").download_fileobj(
            f"{file.user_id}/{file.upload_file_name}", buffer
        )
        buffer.seek(0)
        return buffer, file.file_name

    @staticmethod
    def delete_file(access_user, file_id: int):
        file = File.query.get(file_id)
        if file is None:
            raise ClientError("File not exist")
        if access_user.id != file.user_id:
            raise ForbiddenError

        file.delete()

        s3 = boto3.resource(
            "s3",
            aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
        )
        obj = s3.Object(
            "uploaderfiles", f"{file.user_id}/{file.upload_file_name}"
        )
        response = obj.delete()
        db.session.commit()
        return {"success": True}
