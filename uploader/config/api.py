from flask import Response
from flask import jsonify

from config import api_blueprint

route = api_blueprint.route


@route("/ping")
def ping() -> Response:
    return jsonify({"result": "pong"})
