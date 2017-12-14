from flask import Blueprint
from flask import render_template

cards = Blueprint('cards', __name__,
                  template_folder='templates')


@cards.route('/index')
def show():
    return "cards"


@cards.errorhandler(404)
def page_not_found():
    # return "404"
    return render_template('cards/404.html')
