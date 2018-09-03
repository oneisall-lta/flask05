from App.views import blue


def init_ext(app):
    app.register_blueprint(blue)
