from flask import Blueprint, render_template


blue = Blueprint('blue', __name__)


@blue.route('/goreg')
def go_reg():
    return render_template('register.html')
