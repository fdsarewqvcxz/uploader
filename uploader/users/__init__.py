from flask import Blueprint

api_blueprint = Blueprint(__name__, __name__)
controller = None


def create_endpoints(_controller) -> Blueprint:
    global api_blueprint
    global controller
    controller = _controller

    from users import api

    return api_blueprint
