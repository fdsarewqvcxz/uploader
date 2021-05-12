from flask import jsonify
from flask import request
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required

from folders import api_blueprint
from folders import controller

route = api_blueprint.route


@route("/folders", methods=["POST"])
@jwt_required()
def create_folder():
    data = controller.create_folder(
        access_user=current_user,
        name=request.json.get("name"),
        parent_id=request.json.get("parent_id"),
    )
    return jsonify(data)


@route("/folders/<int:folder_id>")
@jwt_required()
def get_folder(folder_id: int):
    data = controller.get_folder(access_user=current_user, folder_id=folder_id)
    return jsonify(data)


@route("/folders/<int:folder_id>", methods=["PATCH"])
@jwt_required()
def update_folder(folder_id: int):
    data = controller.update_folder(
        access_user=current_user,
        folder_id=folder_id,
        name=request.json.get("name"),
    )
    return jsonify(data)


@route("/folders/<int:folder_id>", methods=["DELETE"])
@jwt_required()
def delete_folder(folder_id: int):
    data = controller.delete_folder(
        access_user=current_user, folder_id=folder_id
    )
    return jsonify(data)
