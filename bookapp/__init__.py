from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # db = SQLAlchemy(app)  也可以将app注入到db中


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/mydb8?charset=utf8'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    return app
