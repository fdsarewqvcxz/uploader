def register_files(app, url_prefix=None):
    from files.controller import FilesController
    from files import create_endpoints

    files_api_blueprint = create_endpoints(FilesController)
    app.register_blueprint(files_api_blueprint, url_prefix=url_prefix)


def register_users(app, url_prefix=None):
    from users.controller import UserController
    from users import create_endpoints

    files_api_blueprint = create_endpoints(UserController)
    app.register_blueprint(files_api_blueprint, url_prefix=url_prefix)
