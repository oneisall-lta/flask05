from flask import Blueprint

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return "<h3 style='color:red'>项目拆分</h3>"
