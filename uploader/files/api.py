import base64

from files import api_blueprint, controller
from flask import jsonify, request, send_file
from flask_jwt_extended import current_user, jwt_required

route = api_blueprint.route


@route("/files", methods=["POST"])
@jwt_required()
def create_file():
    # file = request.files.get("file")
    data = controller.create_file(
        access_user=current_user,
        file=base64.b64decode(request.json.get("file")),
        filename=request.json.get("filename"),
        folder_id=request.json.get("folder_id"),
    )
    return jsonify(data)


@route("/files/<int:file_id>")
@jwt_required()
def get_file(file_id: int):
    file, file_name = controller.get_file(
        access_user=current_user, file_id=file_id
    )
    return send_file(file, attachment_filename=file_name, as_attachment=True)


@route("/files/<int:file_id>", methods=["DELETE"])
@jwt_required()
def delete_file(file_id: int):
    data = controller.delete_file(access_user=current_user, file_id=file_id)
    return jsonify(data)
