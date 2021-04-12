from datetime import timedelta

from flask import Blueprint

from utils import load_json


api_blueprint = Blueprint(__name__, __name__)


class Config:
    secret_json = load_json("secret.json")
    SECRET_KEY = secret_json["secret_key"]
    SQLALCHEMY_DATABASE_URI = secret_json["database_uri"]
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "JWT"
    JWT_IDENTITY_CLAIM = "identity"
    JWT_TOKEN_LOCATION = "headers"


def create_endpoints():
    global api_blueprint

    from config import api

    return api_blueprint
