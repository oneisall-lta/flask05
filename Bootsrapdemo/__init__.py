from flask import Flask
from flask_bootstrap import Bootstrap
from Bootsrapdemo.views import blue


def create_app():
    app = Flask(__name__)
    Bootstrap(app)  # 注册app
    app.register_blueprint(blueprint=blue)
    return app
