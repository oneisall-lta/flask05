from flask import Blueprint, render_template

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return render_template('index.html')
