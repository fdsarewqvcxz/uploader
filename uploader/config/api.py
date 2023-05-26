from config import api_blueprint
from flask import Response, jsonify

route = api_blueprint.route


@route("/ping")
def ping() -> Response:
    return jsonify({"result": "pong"})
