from flask import Flask

from blueprints import register_files
from blueprints import register_users
from config import Config
from models import init_db
from users.jwt import init_jwt


def create_app(config):
    new_app = Flask(__name__)
    new_app.config.from_object(config)
    init_db(new_app)
    init_jwt(new_app)
    register_files(new_app)
    register_users(new_app)
    return new_app


app = create_app(Config)
