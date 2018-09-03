from flask import Flask

from App import settings
from App.ext import init_ext


def create_app(version):
    app = Flask(__name__)
    app.config.from_object(settings.config.get(version))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/mydb8?charset=utf8'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    init_ext(app)  # 向app中注册蓝图，app.register_blueprint(blue);
    # blue
    return app