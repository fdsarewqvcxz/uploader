from flask import Blueprint

api_blueprint = Blueprint("files", __name__)
controller = None


def create_endpoints(_controller):
    global api_blueprint
    global controller
    controller = _controller

    from files import api

    return api_blueprint
