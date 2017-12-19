from flask import Blueprint
from flask import render_template

cards = Blueprint('cards', __name__,
                  template_folder='templates')


@cards.route('/index')
def show():
    # return "cards"
    return render_template('cards/ok.html')

