from flask import Flask
from Cachedemo.views import cache, blue


def create_app():
    app = Flask(__name__)
    cache.init_app(app)
    app.register_blueprint(blueprint=blue)
    return app
